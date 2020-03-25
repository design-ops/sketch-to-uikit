require 'xcodeproj'
require 'fileutils'
require 'optparse'

# add file to the project
# - file_path: of the file to add to the project
# - group: group in xCode project
# - project: xCode project
def add_file(file_path, group, project)
    file = group.new_file(file_path)
    if file.last_known_file_type == 'folder.assetcatalog' # check if is asset catalog to add as a resource
        project.native_targets.each { |target| target.add_resources([file]) if !target.test_target_type? }
    else
        project.native_targets.each { |target| target.add_file_references([file]) if !target.test_target_type? }
    end
end

# create a xCode group in main group. if the group already exist the group will be deleted and create again
def create_group(group_name, project)
    project.main_group.groups.each do |group|
        if group.name == group_name
            group.remove_from_project()
        end
    end

    puts ''
    puts '---------------------'
    puts '🗂  Creating group  🗂'
    puts '---------------------'
    puts ''

    puts '💾  Creating group "' + group_name + '" on ' + project.path.to_s

    group = project.main_group.new_group(group_name)
    return group
end

# copy all files from `path_from` to `path_to`
def copy_files(path_from, path_to)
    FileUtils.mkdir_p(path_to)
    files = Dir[path_from + '/*']
    
    puts ''
    puts '-------------------'
    puts '🚚  Copying files  🚚'
    puts '-------------------'
    puts ''

    files.each do |file|
        if File.directory?(file)
            FileUtils.cp_r(file, path_to)
        else
            FileUtils.cp(file, path_to)
        end

        puts '✅  Copied - ' + File.basename(file)
    end
end

# add all the files from `path` to the project
def add_files_to_project(path, group, project)
    files = Dir[path + '/*']

    puts ''
    puts '------------------------------'
    puts '💻  Add files to the project 💻'
    puts '------------------------------'
    puts ''

    # add files to project
    files.each do |file|
        add_file(file, group, project)
        puts '✅  Added to the project - ' + File.basename(file)
    end
end

# delete (and remove from project) stylist files.
# the files is only deleted when some file is missed. 
def delete_old_files(path_from, project_path, projects)
    files = Dir[path_from + '/*']
    all_files = Dir.glob(project_path + '/**/*') # get all the files in project path
    files_in_workspace = files_in_workspace(projects, project_path).select{ |f| f.class != NilClass }

    puts ''
    puts '---------------------'
    puts '📂  Deleting files  📂'
    puts '---------------------'
    puts ''

    files.each do |file|
        all_files.each do |file_in_disk|
            if File.basename(file) == File.basename(file_in_disk) 
                if File.directory?(file_in_disk)
                    FileUtils.rmdir(file_in_disk)
                else
                    FileUtils.rm(file_in_disk)
                end

                puts '🗑  Delete - ' + File.basename(file)
            end
        end       

        files_in_workspace.each do |file_in_workspace|
            if File.basename(file) == File.basename(file_in_workspace.path)
                file_in_workspace.remove_from_project()
                puts '🗑  Remove from project - ' + File.basename(file)
            end
        end
    end
end

# get all the files in workspace
# get all the files in all workspace project and targets
def files_in_workspace(projects, project_path)
    files_in_workspace = Array.new
    projects.each do |project|
        project.targets.each do |target|
            if target.is_a? Xcodeproj::Project::Object::PBXNativeTarget
                # get source files
                source_files_in_project = target.source_build_phase.files.to_a.map do |pbx_build_file|
                    pbx_build_file.file_ref        
                end

                # get resource files (e.g. assets)
                resources_files_in_project = target.resources_build_phase.files.to_a.map do |pbx_build_file|
                    pbx_build_file.file_ref        
                end

                files_in_project = (source_files_in_project + resources_files_in_project).select { |f| f.class != NilClass and f.path.class != NilClass }
                files_in_project.each do |f|
                    files_in_workspace.push(f)
                end
            end
        end
    end
    return files_in_workspace
end

# find the files in `path_from` and replace in `project_path` (and project)
# it returns true if find all the files and false if some file is missing
def find_files_and_replace(path_from, project_path, projects)
    files = Dir[path_from + '/*']
    all_files = Dir.glob(project_path + '/**/*')
    files_in_workspace = Array.new
    files_in_workspace = files_in_workspace(projects, project_path)
    files_in_workspace = files_in_workspace.select { |f| f.class != NilClass }.map { |f| File.basename(f.path)}

    puts ''
    puts '----------------------'
    puts '📂  Replacing files  📂'
    puts '----------------------'
    puts ''

    files.each do |file|
        find_file = false
        all_files.each do |file_in_disk|
            if File.basename(file) == File.basename(file_in_disk) && files_in_workspace.include?(File.basename(file))
                if File.directory?(file)
                    FileUtils.rmdir(file_in_disk)
                    FileUtils.cp_r(file, File.dirname(file_in_disk))
                else
                    FileUtils.cp(file, file_in_disk)
                end
                puts '✅  Replaced - ' + File.basename(file_in_disk)
                find_file = true
                break
            end
        end
        if !find_file
            puts ''
            puts '------------------------------------------------------------------------'
            puts '❗️️️❗️ ' + File.basename(file) + ' - is missing ❗️️❗️'
            puts ''
            puts ' ⚠️  All the files will be removed and add again to a new project group.'
            puts '------------------------------------------------------------------------'
            return false
        end
    end
    return true
end

# find workspace in path
def workspace_in_path(path)
    files = Dir[path + '/*'].select { |e| File.extname(e) == '.xcworkspace' }
    workspace_path = files.first
    return Xcodeproj::Workspace.new_from_xcworkspace(workspace_path)
end

# find project in path
def project_in_path(path)
    files = Dir[path + '/*'].select { |e| File.extname(e) == '.xcodeproj' }
    project_in_path = files.first
    return Xcodeproj::Project.open(project_in_path)
end

def parse_options() 
    options = {}
    optparse = OptionParser.new do |parser|
        parser.on("-iPATH", "--input=PATH", "Path of result files from sketch generator") do |n|
            options[:input] = n
        end
        parser.on("-aPATH", "--aplication=PATH", "Path of xCode project") do |n|
            options[:aplication] = n
        end
    
        parser.on("-oPATH", "--output=PATH", "Output path (DEFAULT = {Project Path}/Vendor/StylableUIKit)") do |n|
            options[:output] = n
        end
    
        parser.on("-gNAME", "--group=NAME", "xCode group name (DEFAULT = StylableUIKit") do |n|
            options[:group] = n
        end
    
        parser.on( '-h', '--help', 'Help' ) do
            puts parser
            exit
          end
    end
    
    optparse.parse!
    # mandatory parameters
    if options[:input].nil? or options[:aplication].nil?
        abort(optparse.help)
    end

    return options
end

options = parse_options()
default_group = options[:group].nil? ? 'StylableUIKit' : options[:group]
project_path = options[:aplication]
source_files_path = options[:input]
result_path = options[:output].nil? ? project_path + '/Vendor/StylableUIKit' : options[:output]
workspace = workspace_in_path(project_path)
projects = workspace.file_references.map { |project_name|  Xcodeproj::Project.open(project_path + '/' + project_name.path) }
project = projects[0]

# check if all the files exist in the project directory and in project. and update files.
need_to_reset = find_files_and_replace(source_files_path, project_path, projects)
if !need_to_reset 
    # if don't exist need to delete all the files
    delete_old_files(source_files_path, project_path, projects)
    copy_files(source_files_path, result_path)
    group = create_group(default_group, project)
    add_files_to_project(result_path, group, project)
end
puts ''
puts '----------------------'
puts '💾  Saving projects  💾'
puts '----------------------'
puts ''

projects.each do |project|
    puts '💾  Saving project ' + project.path.to_s
    project.save()
end
puts ''
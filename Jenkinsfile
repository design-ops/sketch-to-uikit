pipeline {
    agent { label 'jenkins-base-agent' }
    stages {
        stage ('Build Container') {
            steps {
                sh 'bin/setup'
            }
        }
        stage ('Testing') {
            steps {
                sh 'bin/test'
            }
        }
    }
}

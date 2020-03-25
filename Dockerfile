FROM swift:4.2.2

RUN apt-get -q update \
    && apt-get -q install -y \
    jq \
    build-essential git libreadline-dev zlib1g-dev libssl-dev libbz2-dev libsqlite3-dev ruby

RUN gem install xcodeproj

ENV PYENV_ROOT="/.pyenv" \
    PATH="/.pyenv/bin:/.pyenv/shims:$PATH" \
    PYTHONPATH="$PYTHONPATH:./src"

# install pyenv to install Python 3.7
RUN curl -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash \
    && pyenv install 3.7.2 \
    && pyenv global 3.7.2

# install swiftformat
RUN git clone https://github.com/nicklockwood/SwiftFormat \
    && cd SwiftFormat \
    && swift build -c release \
    && mv .build/release/swiftformat /usr/bin/swiftformat

WORKDIR /work

COPY . /work

RUN python --version \
    && pip --version

RUN pip install --no-cache-dir -r requirements.txt

#CMD python app.py --help

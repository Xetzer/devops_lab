#!/bin/bash

echo "Installing python:"
sudo yum install -y zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel openssl-devel xz xz-devel
curl -L https://raw.github.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bash_profile
source ~/.bash_profile
pyenv install 2.7.14
pyenv install 3.5.4
echo "Available python vesrions:"
pyenv versions
echo "Creating environments:"
pyenv global 2.7.14
pyenv virtualenv venv2.7
pyenv global 3.5.4
pyenv virtualenv venv3.5
echo "Available environments:"
pyenv virtualenvs


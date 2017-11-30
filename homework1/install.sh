#!/bin/bash

echo "Installing dependencies:"
sudo yum install -y zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel openssl-devel xz xz-devel
curl -L https://raw.github.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
echo "Adding variables:"
if ! grep -q 'export PYENV_ROOT="$HOME/.pyenv"' ~/.bashrc; then
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
fi
if ! grep -q 'export PATH="$PYENV_ROOT/bin:$PATH"' ~/.bashrc; then
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
fi
if ! grep -q 'eval "$(pyenv init -)"' ~/.bashrc; then
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
fi
if ! grep -q 'eval "$(pyenv virtualenv-init -)"' ~/.bashrc; then
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
fi
source ~/.bashrc
echo "Installing python:"
if ! [ -d  ~/.pyenv/versions/2.7.14/ ]; then
echo "Installing python 2.7.14"
pyenv install 2.7.14
fi
if ! [ -d ~/.pyenv/versions/3.5.4/ ]; then
echo "Installing python 3.5.4"
pyenv install 3.5.4
fi
echo "Available python vesrions:"
pyenv versions
echo "Creating environments:"
pyenv global 2.7.14
pyenv virtualenv venv2.7
pyenv global 3.5.4
pyenv virtualenv venv3.5
echo "Available environments:"
pyenv virtualenvs

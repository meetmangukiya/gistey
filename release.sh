set -e
sudo pip3 install --upgrade pip
sudo pip3 install --upgrade setuptools
sudo pip3 install --upgrade twine

python3 autoversion.py --type dev
python3 setup.py bdist_wheel sdist


source rultor_secrets.sh

set +e
twine upload dist/* -u "$USER" -p "$PWD"
set -e

rm -r build dist gistey.egg-info

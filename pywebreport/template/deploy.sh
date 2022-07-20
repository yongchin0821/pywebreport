# 确保脚本抛出遇到的错误
set -e

# gen dist
rm -rf dist
mkdir dist
cp ../../test/testsuites/pytest/result/report.html dist/
cp ../../test/testsuites/pytest/result/report.css dist/
cp ../../test/testsuites/pytest/result/city.png dist/

# cd folder
cd dist
git init
git add -A
git commit -m 'deploy'

git push -f https://github.com/yongchin0821/pywebreport.git main:gh-pages

cd -

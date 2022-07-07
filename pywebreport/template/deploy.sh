# 确保脚本抛出遇到的错误
set -e

# gen dist
rm -rf dist
mkdir dist
cp index.html dist/
cp report.css dist/
cp city.png dist/

# cd folder
cd dist
git init
git add -A
git commit -m 'deploy'

git push -f https://github.com/yongchin0821/pywebreport.git main:gh-pages

cd -

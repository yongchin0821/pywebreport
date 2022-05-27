# 确保脚本抛出遇到的错误
set -e

# 生成dist
rm -rf dist
mkdir dist
cp index.html dist/
cp report.css dist/
cp city.png dist/

# 进入生成的文件夹
cd dist
git init
git add -A
git commit -m 'deploy'

# 如果发布到 https://SeldomQA.github.io
git push -f https://github.com/yongchin0821/pywebreport.git main:gh-pages

cd -

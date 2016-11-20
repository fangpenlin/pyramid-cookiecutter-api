git init
git remote add origin git@github.com:victorlin/pyramid_api.git
git fetch
git branch -t master origin/master
git add --all
git commit -m "Archive of $CIRCLE_SHA1"
git push origin master

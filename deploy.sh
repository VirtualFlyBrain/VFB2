#Copyright 2018 Google LLC
#
#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.
#
HUGO_ENV="production"

set -x




cd /src/

npm install -g npm

npm install --global yarn

npm install --save-dev autoprefixer postcss-cli postcss

cd /src/themes/docsy/ 
npm install

cd /src/

hugo --enableGitInfo --gc -v

hugo mod clean --all

hugo mod graph

hugo --enableGitInfo --gc -v

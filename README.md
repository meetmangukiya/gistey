# `gist`

## Usage:

1. To create a public gist with description for a bunch of files
   ```
   $ gist --description "This would be the description" --files somefile.ext someotherfile

   URL of the gist created:  https://gist.github.com/b74c057c1fc9de92402f86cbe3979dfa
   ```

2. To create a secret gist, just add `--secret` option
   ```
   $ gist --description "This would be the description" --files somefile.ext someotherfile --secret

   URL of the gist created:  https://gist.github.com/<id>
   ```

3. To create a gist without description
   ```
   $ gist --files somefile.ext someotherfile

   URL of the gist created:  https://gist.github.com/b74c057c1fc9de92402f86cbe3979dfa
   ```

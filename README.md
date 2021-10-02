# My Scripts

[![CodeFactor](https://www.codefactor.io/repository/github/baggiponte/scripts/badge)](https://www.codefactor.io/repository/github/baggiponte/scripts)

I am starting to write custom `bash` scripts to speed up some operations, and I am learning a great deal of stuff. I am putting these here, hoping they will be of help for someone!

## Scripts Descriptions

* **clean_headers**. Transforms the headers of a `.csv` file to snakecase.
* **conda_update_all_envs**. Updates all conda envs. *To be made interactive!*
* **count_freq**. Counts frequencies of a variable in a `.csv` file.
* **make_journal_entry**. Creates a new entry for a research journal. Useful to improve upon to create parametrised files or templates.
* **pg_server_status**. Checks if the `PostgreSQL` server is running, else starts it. *Have the $PGDATA/input dir read from input*

## To Do List

* [ ] rewrite scripts using functions
* `brew_export`:
    * [ ] make the function generate a `.json` timestamp and schedule a `cron` job or GitHub Workflow?
    * [ ] make the script check if the packages are the same and then not override it? 
* [ ] add `read` section to `conda_backup_env` to prevent automatic removal of the env.

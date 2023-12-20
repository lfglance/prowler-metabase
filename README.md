# Prowler report visualizer

Uses metabase to visualize Prowler scan reports.

Runs a PostgreSQL database with a custom Python script to load data from Prowler CSV exports.


## Install

on MacOS:

```bash
xcode-select --install
brew install postgresql gcc docker-compose docker
```

## Notes

```bash
docker run --rm -d -p 3000:3000 \
  -v $PWD/data:/metabase-data \
  -v $PWD/plugins:/plugins \
  -e "MB_DB_FILE=/metabase-data/metabase.db" \
  --name metabase metabase/metabase

mkdir plugins
wget https://github.com/Markenson/csv-metabase-driver/releases/download/v1.3.1/csv.metabase-driver.jar \
  -O plugins/csv.metabase-driver.jar

docker logs -f metabase
```


```
df[(df.CheckType.apply(lambda x: ''.join(x)) == 'IAM') & (df.Status == 'FAIL')].shape[0]
```
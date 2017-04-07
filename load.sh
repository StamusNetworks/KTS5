#!/bin/bash
set -e
set -x

cd $(dirname $0)

function get_name()
{
	basename "$1" .json | sed -e 's/ /%20/g'
}

if [ -z "$1" ]; then
    ELASTICSEARCH=http://127.0.0.1:9200
else
    ELASTICSEARCH=$1
fi

if [ -z "$2" ]; then
    CURL=curl
else
    CURL="curl --user $2"
fi

echo $CURL
DIR=dashboards

echo "Cleaning elasticsearch's kibana data"
$CURL -XDELETE $ELASTICSEARCH/.kibana/ ||:

for file in $DIR/index-pattern/*.json
do
    name="$(get_name "$file")"
    echo "Loading index pattern $name:"

    $CURL -XPOST "$ELASTICSEARCH/.kibana/index-pattern/$name" \
        -d "@$file" || exit 1
    echo
done


for file in $DIR/search/*.json
do
    name="$(get_name "$file")"
    echo "Loading search $name:"
    $CURL -XPUT "$ELASTICSEARCH/.kibana/search/$name" \
        -d "@$file" || exit 1
    echo
done

for file in $DIR/visualization/*.json
do
    name="$(get_name "$file")"
    echo "Loading visualization $name:"
    $CURL -XPUT "$ELASTICSEARCH/.kibana/visualization/$name" \
        -d "@$file" || exit 1
    echo
done

for file in $DIR/dashboard/*.json
do
    name="$(get_name "$file")"
    echo "Loading dashboard $name:"
    $CURL -XPUT "$ELASTICSEARCH/.kibana/dashboard/$name" \
        -d "@$file" || exit 1
    echo
done

echo "Loading config:"
$CURL -XPOST $ELASTICSEARCH/.kibana/config/4.3.1 \
        -d @dashboards/config.json || exit 1

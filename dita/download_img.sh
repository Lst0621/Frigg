#!/bin/bash

mkdir data
web_url="https://www.vmfa.museum/piction/108734640-200940384"
curl $web_url > data/dita.html

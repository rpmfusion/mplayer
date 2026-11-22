#!/bin/bash


set -e

pwd=$(pwd)
package=mplayer.git
branch=master
name=mplayer

if [ ! -d ${package} ]; then
    git clone https://git.ffmpeg.org/mplayer.git mplayer.git
fi

pushd ${package}
git checkout ${branch}
git pull

version=$(git rev-list --count --first-parent HEAD)
date=$(git log -1 --format=%cd --date=format:%Y%m%d)
tag=$(git rev-parse --short=7 HEAD)

TARFILE=${pwd}/${name}-${version}-${date}-${tag}.tar
echo git archive --prefix="${name}-${version}/" --format=tar ${branch} \> ${TARFILE}
git archive --prefix="${name}-${version}/" --format=tar ${branch} > ${TARFILE}
popd

bzip2 ${TARFILE}

echo \# globals for ${name}-${version}-${date}-${tag}.tar.bz2
echo %global gitversion  ${version}
echo %global gitdate    ${date}
echo %global gittag     ${tag}
sed -i "s|^# globals for .*|# globals for ${name}-${version}-${date}-${tag}.tar.bz2|" mplayer.spec
sed -i "s|^%global gitversion .*|%global gitversion ${version}|" mplayer.spec
sed -i "s|^%global gitdate .*|%global gitdate ${date}|" mplayer.spec
sed -i "s|^%global gittag .*|%global gittag ${tag}|" mplayer.spec


#!/bin/bash

set -e

tmp=$(mktemp -d)

trap cleanup EXIT
cleanup() {
    set +e
    [ -z "$tmp" -o ! -d "$tmp" ] || rm -rf "$tmp"
}

unset CDPATH
pwd=$(pwd)
svn=$(date +%Y-%m-%d)
dirname=mplayer-export-$svn

cd "$tmp"
svn checkout -r {$svn} svn://svn.mplayerhq.hu/mplayer/trunk $dirname
cd $dirname
rm -rf libdvdcss
for dir in libav* libpostproc ; do
	cd $dir
	svn update -r {$svn}
	cd ..
done
svn_revision=`LC_ALL=C svn info 2> /dev/null | grep Revision | cut -d' ' -f2`
sed -i -e 's/\(SVN-r[0-9]* \)/\1rpmfusion /' -e "s/UNKNOWN/$svn_revision/" version.sh
find . -type d -name .svn -print0 | xargs -0r rm -rf
cd ..
tar jcf "$pwd"/$dirname.tar.bz2 $dirname
cd - >/dev/null

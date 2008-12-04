%define         codecdir %{_libdir}/codecs
%define         pre 20081204svn
%define         svn 1
%define         svnbuild 2008-12-04
%define         faad2min 1:2.6.1

Name:           mplayer
Version:        1.0
Release:        0.104.%{pre}%{?dist}
Summary:        Movie player playing most video formats and DVDs

Group:          Applications/Multimedia
License:        GPLv2+
URL:            http://www.mplayerhq.hu/
%if %{svn}
# run ./mplayer-snapshot.sh to get this
Source0:        mplayer-export-%{svnbuild}.tar.bz2
%else
Source0:        http://www.mplayerhq.hu/MPlayer/releases/MPlayer-%{version}%{pre}.tar.bz2
%endif
Source1:        http://www.mplayerhq.hu/MPlayer/skins/Blue-1.7.tar.bz2
Source10:       mplayer-snapshot.sh
Patch2:         %{name}-config.patch
Patch5:         %{name}-x86_32-compile.patch
Patch8:         %{name}-manlinks.patch
Patch10:        %{name}-qcelp.patch
Patch12:        %{name}-man-zh_CN.patch
Patch14:        %{name}-nodvdcss.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  SDL-devel
BuildRequires:  aalib-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  cdparanoia-devel
BuildRequires:  desktop-file-utils
BuildRequires:  em8300-devel
BuildRequires:  enca-devel
BuildRequires:  faac-devel
BuildRequires:  faad2 >= %{faad2min}
BuildRequires:  faad2-devel >= %{faad2min}
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel >= 2.0.9
BuildRequires:  fribidi-devel
BuildRequires:  giflib-devel
BuildRequires:  gtk2-devel
BuildRequires:  ladspa-devel
BuildRequires:  lame-devel
BuildRequires:  libGL-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXScrnSaver-devel
BuildRequires:  libXv-devel
BuildRequires:  libXvMC-devel
BuildRequires:  libXxf86dga-devel
BuildRequires:  libXxf86vm-devel
BuildRequires:  libcaca-devel
BuildRequires:  libdca-devel
BuildRequires:  libdv-devel
BuildRequires:  libdvdnav-devel >= 4.1.3-0.4
BuildRequires:  libjpeg-devel
BuildRequires:  libmpcdec-devel
BuildRequires:  libtheora-devel
BuildRequires:  libvorbis-devel
BuildRequires:  lirc-devel
BuildRequires:  live555-devel
BuildRequires:  lzo-devel >= 2
BuildRequires:  pulseaudio-lib-devel
BuildRequires:  speex-devel >= 1.1
BuildRequires:  twolame-devel
BuildRequires:  x264-devel >= 0.0.0-0.14.20080613
BuildRequires:  xvidcore-devel >= 0.9.2
%{?_with_arts:BuildRequires: arts-devel}
%{?_with_amr:BuildRequires: amrnb-devel amrwb-devel}
%{?_with_directfb:BuildRequires: directfb-devel}
%{?_with_esound:BuildRequires: esound-devel}
%{?_with_jack:BuildRequires: jack-audio-connection-kit-devel}
%{?_with_libmad:BuildRequires:  libmad-devel}
%{?_with_nemesi:BuildRequires:  libnemesi-devel >= 0.6.3}
%{?_with_openal:BuildRequires: openal-devel}
%{?_with_samba:BuildRequires: libsmbclient-devel}
%{?_with_svgalib:BuildRequires: svgalib-devel}
%{?_with_xmms:BuildRequires: xmms-devel}
%if %{svn}
# for XML docs, SVN only
BuildRequires:  docbook-dtds
BuildRequires:  docbook-style-xsl
BuildRequires:  libxml2
BuildRequires:  libxslt
%endif
Obsoletes:      mplayer-fonts
Requires:       faad2-libs >= %{faad2min}

%description
MPlayer is a movie player that plays most MPEG, VOB, AVI, OGG/OGM,
VIVO, ASF/WMA/WMV, QT/MOV/MP4, FLI, RM, NuppelVideo, yuv4mpeg, FILM,
RoQ, and PVA files. You can also use it to watch VCDs, SVCDs, DVDs,
3ivx, RealMedia, and DivX movies.
It supports a wide range of output drivers including X11, XVideo, DGA,
OpenGL, SVGAlib, fbdev, AAlib, DirectFB etc. There are also nice
antialiased shaded subtitles and OSD.
Non-default rpmbuild options:
--with samba:   Enable Samba (smb://) support
--with xmms:    Enable XMMS input plugin support
--with amr:     Enable AMR support
--with libmad:  Enable libmad support
--with openal:  Enable OpenAL support
--with jack:    Enable JACK support
--with arts:    Enable aRts support
--with esound:  Enable EsounD support
--with directfb:Enable DirectFB support
--with svgalib: Enable SVGAlib support
--with nemesi:  Enable libnemesi RTSP support

%package        gui
Summary:        GUI for MPlayer
Group:          Applications/Multimedia
Requires:       mplayer = %{version}-%{release}
Requires:       hicolor-icon-theme

%description    gui
This package contains a GUI for MPlayer and a default skin for it.

%package     -n mencoder
Summary:        MPlayer movie encoder
Group:          Applications/Multimedia
Requires:       mplayer = %{version}-%{release}

%description -n mencoder
This package contains the MPlayer movie encoder. 

%package        doc
Summary:        MPlayer documentation in various languages
Group:          Documentation

%description    doc
MPlayer documentation in various languages.

%define mp_configure \
./configure \\\
    --prefix=%{_prefix} \\\
    --bindir=%{_bindir} \\\
    --datadir=%{_datadir}/mplayer \\\
    --mandir=%{_mandir} \\\
    --confdir=%{_sysconfdir}/mplayer \\\
    --libdir=%{_libdir} \\\
    --codecsdir=%{codecdir} \\\
    \\\
    --target=%{_target_cpu}-%{_target_os} \\\
    --language=all \\\
    \\\
    --enable-joystick \\\
    --enable-largefiles \\\
    --enable-lirc \\\
    --enable-menu \\\
    --enable-runtime-cpudetection \\\
    --enable-unrarexec \\\
    \\\
    --disable-dvdread-internal \\\
    --disable-libdvdcss-internal \\\
    %{!?_with_nemesi:--disable-nemesi} \\\
    %{!?_with_samba:--disable-smb} \\\
    \\\
    --disable-faac-lavc \\\
    --disable-mp3lame-lavc \\\
    --disable-x264-lavc \\\
    \\\
    %{!?_with_amr:--disable-libamr_nb --disable-libamr_wb} \\\
    --disable-faad-internal \\\
    %{!?_with_libmad:--disable-mad} \\\
    --disable-tremor-internal \\\
    %{?_with_xmms:--enable-xmms} \\\
    %{?_with_xmms:--with-xmmslibdir=%{_libdir}} \\\
    \\\
    --disable-bitmap-font \\\
    --%{?_with_directfb:enable}%{!?_with_directfb:disable}-directfb \\\
    --with-fribidi-config="pkg-config fribidi" \\\
    %{!?_with_svgalib:--disable-svga} \\\
    --disable-termcap \\\
    --enable-xvmc \\\
    --with-xvmclib=XvMCW \\\
    \\\
    %{!?_with_arts:--disable-arts} \\\
    %{!?_with_esound:--disable-esd} \\\
    %{!?_with_jack:--disable-jack} \\\
    %{!?_with_openal:--disable-openal} \\\


%prep
%if %{svn}
%setup -q -n mplayer-export-%{svnbuild}
%else
%setup -q -n MPlayer-%{version}%{pre}
%endif
%patch2 -p1 -b .config
%patch5 -p1 -b .compile
%patch8 -p1 -b .manlinks
%patch10 -p1 -b .qclp
%patch12 -p1 -b .man-zh_CN
%patch14 -p1 -b .nodvdcss

doconv() {
    iconv -f $1 -t $2 -o DOCS/man/$3/mplayer.1.utf8 DOCS/man/$3/mplayer.1 && \
    mv DOCS/man/$3/mplayer.1.utf8 DOCS/man/$3/mplayer.1
}
for lang in de es fr it ; do doconv iso-8859-1 utf-8 $lang ; done
for lang in hu pl ; do doconv iso-8859-2 utf-8 $lang ; done
for lang in ru ; do doconv koi8-r utf-8 $lang ; done

mv DOCS/man/zh DOCS/man/zh_CN

%build
export CFLAGS="$RPM_OPT_FLAGS -ffast-math --std=gnu99"
%ifarch ppc
export CFLAGS="$CFLAGS -maltivec -mabi=altivec"
%endif
%{mp_configure}--enable-gui

%{__make} %{?_smp_mflags}

mv -f mplayer gmplayer
%{__make} distclean

%{mp_configure}

%{__make} %{?_smp_mflags}

%if %{svn}
# build HTML documentation from XML files 
pushd DOCS/xml
%{__make} html-chunked
popd
%endif

%install
rm -rf $RPM_BUILD_ROOT doc

make install DESTDIR=$RPM_BUILD_ROOT STRIPBINARIES=no
for file in aconvert.sh midentify.sh ; do
install -pm 755 TOOLS/$file $RPM_BUILD_ROOT%{_bindir}/
done

# Clean up documentation
mkdir doc
cp -pR DOCS/* doc/
rm -r doc/man doc/xml doc/README
mv doc/HTML/* doc/
rm -rf doc/HTML

# Default config files
install -Dpm 644 etc/example.conf \
    $RPM_BUILD_ROOT%{_sysconfdir}/mplayer/mplayer.conf

install -pm 644 etc/{input,menu}.conf $RPM_BUILD_ROOT%{_sysconfdir}/mplayer/

# GUI mplayer
install -pm 755 g%{name} $RPM_BUILD_ROOT%{_bindir}/

# Default skin
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/mplayer/skins
tar xjC $RPM_BUILD_ROOT%{_datadir}/mplayer/skins --exclude=.svn -f %{SOURCE1}
ln -s Blue $RPM_BUILD_ROOT%{_datadir}/mplayer/skins/default

# Icons
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
install -pm 644 etc/mplayer.xpm \
    $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps

# Desktop file
desktop-file-install \
        --vendor livna \
        --dir $RPM_BUILD_ROOT%{_datadir}/applications \
        etc/%{name}.desktop

# Codec dir
install -dm 755 $RPM_BUILD_ROOT%{codecdir}


%post gui
gtk-update-icon-cache -qf %{_datadir}/icons/hicolor &>/dev/null || :
update-desktop-database &>/dev/null || :


%postun gui
gtk-update-icon-cache -qf %{_datadir}/icons/hicolor &>/dev/null || :
update-desktop-database &>/dev/null || :


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-, root, root, -)
%doc AUTHORS Changelog Copyright LICENSE README
%dir %{_sysconfdir}/mplayer
%config(noreplace) %{_sysconfdir}/mplayer/mplayer.conf
%config(noreplace) %{_sysconfdir}/mplayer/input.conf
%config(noreplace) %{_sysconfdir}/mplayer/menu.conf
%{_bindir}/aconvert.sh
%{_bindir}/midentify.sh
%{_bindir}/mplayer
%dir %{codecdir}/
%dir %{_datadir}/mplayer/
%{_mandir}/man1/mplayer.1*
%lang(cs) %{_mandir}/cs/man1/mplayer.1*
%lang(de) %{_mandir}/de/man1/mplayer.1*
%lang(es) %{_mandir}/es/man1/mplayer.1*
%lang(fr) %{_mandir}/fr/man1/mplayer.1*
%lang(hu) %{_mandir}/hu/man1/mplayer.1*
%lang(it) %{_mandir}/it/man1/mplayer.1*
%lang(pl) %{_mandir}/pl/man1/mplayer.1*
%lang(ru) %{_mandir}/ru/man1/mplayer.1*
%lang(zh_CN) %{_mandir}/zh_CN/man1/mplayer.1*

%files gui
%defattr(-, root, root, -)
%{_bindir}/gmplayer
%{_datadir}/applications/*mplayer.desktop
%{_datadir}/icons/hicolor/32x32/apps/mplayer.xpm
%{_datadir}/mplayer/skins/

%files -n mencoder
%defattr(-, root, root, -)
%{_bindir}/mencoder
%{_mandir}/man1/mencoder.1*
%lang(cs) %{_mandir}/cs/man1/mencoder.1*
%lang(de) %{_mandir}/de/man1/mencoder.1*
%lang(es) %{_mandir}/es/man1/mencoder.1*
%lang(fr) %{_mandir}/fr/man1/mencoder.1*
%lang(hu) %{_mandir}/hu/man1/mencoder.1*
%lang(it) %{_mandir}/it/man1/mencoder.1*
%lang(pl) %{_mandir}/pl/man1/mencoder.1*
%lang(ru) %{_mandir}/ru/man1/mencoder.1*
%lang(zh_CN) %{_mandir}/zh_CN/man1/mencoder.1*

%files doc
%defattr(-, root, root, -)
%doc doc/en/ doc/tech/
%lang(cs) %doc doc/cs/
%lang(de) %doc doc/de/
%lang(es) %doc doc/es/
%lang(fr) %doc doc/fr/
%lang(hu) %doc doc/hu/
%lang(pl) %doc doc/pl/
%lang(ru) %doc doc/ru/
%lang(zh_CN) %doc doc/zh_CN/


%changelog
* Thu Dec 04 2008 Dominik Mierzejewski <rpm at greysector.net> - 1.0-0.104.20081204svn
- 20081204 snapshot
- dropped obsolete/upstreamed patches

* Sun Nov 23 2008 Dominik Mierzejewski <rpm at greysector.net> - 1.0-0.103.20080903svn
- fix broken terminal after using dvb input (bug #117)
- disable backing store (fixes tearing on Xorg Xserver 1.5.x)
- disable samba support by default, too much dependency bloat (bug #147)
- add missing Requires for hicolor icon dirs to -gui
- drop provides and obsoletes for mplayer-mencoder (last seen for FC4)

* Tue Oct 28 2008 Dominik Mierzejewski <rpm at greysector.net> - 1.0-0.102.20080903svn
- rework the build system
- rebuild for new libcaca

* Thu Oct 16 2008 Dominik Mierzejewski <rpm at greysector.net> - 1.0-0.101.20080903svn
- remove libdvdcss copy from the source tarball

* Sun Oct 12 2008 Dominik Mierzejewski <rpm at greysector.net> - 1.0-0.100.20080903svn
- backport the fix for CVE-2008-3827

* Tue Sep 09 2008 Dominik Mierzejewski <rpm at greysector.net> - 1.0-0.99.20080903svn
- updated to 20080903 SVN snapshot
- added snapshot creation script
- dropped version sed-patching (happens in the snapshot script now)
- enabled samba support by default

* Tue Aug 19 2008 Dominik Mierzejewski <rpm at greysector.net> - 1.0-0.98.20080818svn
- moved config settings to config patch
- rebased patches against current snapshot

* Mon Aug 18 2008 Dominik Mierzejewski <rpm at greysector.net> - 1.0-0.97.20080818svn
- updated to latest SVN snapshot
- dropped obsolete patches
- installed aconvert.sh to bindir
- fixed zh_CN manpage installation

* Sun Aug 17 2008 Dominik Mierzejewski <rpm at greysector.net> - 1.0-0.96.20080613svn
- live-devel is now live555-devel
- added missing libXScrnSaver-devel BR
- fixed audio in some rtsp streams (backport from SVN)

* Sat Aug 09 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info - 1.0-0.95.20080613svn
- rebuild

* Sat Jun 14 2008 Dominik Mierzejewski <rpm at greysector.net> - 1.0-0.94.20080613svn
- updated to latest SVN snapshot (bugs #1812, #1910, #1895)
- fixed building with svgalib support
- use pulseaudio output by default
- BR latest libdvdnav
- bring back live (bug #1950), make libnemesi optional
- drop obsolete patches
- fix building against fribidi (bug #1887)
- BR latest x264
- re-enable parallel make

* Sat Mar 15 2008 Thorsten Leemhuis <fedora at leemhuis.info> - 1.0-0.93.20080211svn
- rebuild for new x264

* Mon Feb 11 2008 Dominik Mierzejewski <rpm at greysector.net> - 1.0-0.92.20080211svn
- updated to latest SVN snapshot
- fixed opening files with spaces in their names (bug #1674)
- libnemesi doesn't conflict with live anymore
- fixed samba BR (bug #1809)
- enabled libnemesi by default
- made live optional
- security fixes: CVE-2008-0485, CVE-2008-0486, CVE-2008-0629, CVE-2008-0630
  (bug #1852)

* Mon Dec 03 2007 Dominik Mierzejewski <rpm at greysector.net> - 1.0-0.91.20071201svn
- use correct chanmap patch
- obsolete mplayer-fonts
- require our faad2 2.6.1

* Sat Dec 01 2007 Dominik Mierzejewski <rpm at greysector.net> - 1.0-0.90.20071201svn
- updated to latest SVN snapshot
- reverted a change which requires newer libdvdnav snapshot
- fixed license tag
- use man-links instead of real filesystem symlinks for mencoder.1
- fixed desktop file

* Sun Nov 11 2007 Dominik Mierzejewski <rpm at greysector.net> - 1.0-0.89.rc2
- rebuild against faad2-2.6.1
- drop obsolete patch

* Tue Nov 06 2007 Dominik Mierzejewski <rpm at greysector.net> - 1.0-0.88.rc2
- fixed crash in vorbis decoder (bug #1516)
- added pulseaudio support
- better libnemesi support
- fixed libdca support

* Tue Nov 06 2007 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]info> - 1.0-87
- rebuild

* Sat Oct 13 2007 Dominik Mierzejewski <rpm at greysector.net> - 1.0-0.86.rc2
- work around Fedora bug 330031

* Thu Oct 11 2007 Dominik Mierzejewski <rpm at greysector.net> - 1.0-0.85.rc2
- 1.0rc2
- drop obsolete/useless patches
- add experimental audio channel reordering patch
- optional libnemesi support (mutually exclusive with LIVE555)
- revert to internal faad2 (linking with 2.5 makes MPlayer non-distributable)
  but leave a build-time option
- don't rebuild HTML docs for releases
- include Copyright file

* Thu Sep 27 2007 Dominik Mierzejewski <rpm at greysector.net> - 1.0-0.84.20070923svn
- really fix it this time

* Wed Sep 26 2007 Dominik Mierzejewski <rpm at greysector.net> - 1.0-0.83.20070923svn
- fix build on x86_32

* Wed Sep 26 2007 Dominik Mierzejewski <rpm at greysector.net> - 1.0-0.82.20070923svn
- disable parallel make (fails on vidix)
- re-enable external faad2 (fixed in 2.5-4)

* Sun Sep 23 2007 Dominik Mierzejewski <rpm at greysector.net> - 1.0-0.81.20070923svn
- latest snapshot
- update Blue skin
- fix seeking with -demux lavf
- dropped obsolete patches
- Czech manpage is already utf8 (bug #1626)
- fixes CVE-2007-4938 (bug #1645)
- disable external faad, seems broken

* Sat Jul 21 2007 Dominik Mierzejewski <rpm at greysector.net> - 1.0-0.80.20070715svn
- fix build on i386
- another libdca patch update
- fix parallel builds

* Fri Jul 20 2007 Dominik Mierzejewski <rpm at greysector.net> - 1.0-0.79.20070715svn
- fix a crash in subtitle selection code
- updated libdca patch

* Sun Jul 15 2007 Dominik Mierzejewski <rpm at greysector.net> - 1.0-0.78.20070715svn
- latest snapshot
- use external libfaad again
- restore libdca support
- make ad_faad detect the correct sample rate on 64-bit systems
  (based on a patch by Rasmus Rohde)

* Tue Jun 12 2007 Dominik Mierzejewski <rpm at greysector.net> - 1.0-0.77.20070612svn
- latest snapshot
- dropped one obsolete patch
- fixed CVE-2007-2948 (#1525)
- backported compilation fix from r23546
- dropped redundant BR: libpng-devel (brought in by gtk2-devel)

* Tue May 15 2007 Dominik Mierzejewski <rpm at greysector.net> - 1.0-0.75.20070513svn
- BuildRequire the new libdvdnav

* Sun May 13 2007 Dominik Mierzejewski <rpm at greysector.net> - 1.0-0.74.20070513svn
- 20070513 snapshot
- libdha is now static

* Sun Mar 25 2007 Dominik Mierzejewski <rpm at greysector.net> - 1.0-0.72.20070325svn
- 20070325 snapshot
- built with internal libav{codec,format,util}
- dropped obsolete patches

* Sun Mar 18 2007 Dominik Mierzejewski <rpm at greysector.net> - 1.0-0.71.rc1
- fix buffer overflow in DS_VideoDecoder.c (bug #1443)

* Sat Mar 10 2007 Dominik Mierzejewski <rpm at greysector.net> - 1.0-0.70.rc1
- fix buffer overflow in DMO_VideoDecoder.c

* Wed Jan 03 2007 Dominik Mierzejewski <rpm at greysector.net> - 1.0-0.69.rc1                                          
- fix buffer overflow in asmrp.c 

* Thu Dec 28 2006 Dominik Mierzejewski <rpm at greysector.net> - 1.0-0.68.rc1
- don't depend on urw-fonts, use generic Sans font instead

* Tue Dec 26 2006 Dominik Mierzejewski <rpm at greysector.net> - 1.0-0.67.rc1
- disable bitmap fonts
- add libdca support
- add twolame support
- prevent linking mplayer with GUI libs
- make libmad support optional

* Sun Nov  5 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.0-0.66.rc1
- Apply upstream mp3lib workaround instead of disabling 3DNow altogether in it,
  thanks to Dominik 'Rathann' Mierzejewski.

* Tue Oct 31 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.0-0.65.rc1
- 1.0rc1, ffmpeg WMV3 patch applied upstream.
- Include libdvdnav and x264 support.

* Fri Oct 06 2006 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> 1.0-64
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Tue Sep 26 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.0-0.63.pre8
- Rebuild.

* Fri Aug 18 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.0-0.62.pre8
- Enable ffmpeg WMV3 decoder.
- Work around hang when dumping to wav on ix86 (#1127).
- Disable internal tremor due to above workaround making it crashy.
- Disable FriBidi (#612) and joystick (#983) in default config file.
- Specfile/build dependency cleanups.
- Update default Blue skin to 1.6.

* Thu Jul 27 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.0-0.61.pre8
- Move codecs dir to %%{_libdir}/codecs to follow upstream, old location
  in %%{_libdir}/win32 still appears to work as a fallback.
- Ship codecs dir on all architectures again.

* Thu Jul 27 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.0-0.60.pre8
- Make DirectFB support optional, disabled by default (#1102).
- Adapt to lzo2, require it.
- Include midentify (#1105).

* Mon Jun 26 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.0-0.44.pre8
- System wide skins dir has changed to /usr/share/mplayer/skins (#1070).

* Thu Jun 22 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.0-0.42.pre8
- Make arts and esound support optional, disabled by default (#1067).
- Specfile and legacy dependency cleanups.

* Fri Jun 16 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.0-0.40.pre8
- 1.0pre8.
- Drop runtime CPU detection message removal patch.
- Disable XMMS and OpenAL support by default.
- Add support for building with JACK support, disabled by default.
- Don't include the %%{_libdir}/win32 dir on non-x86.
- Fix %%lang tags in -doc.

* Sat May 13 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.0-0.39.20060513
- 2006-05-13 CVS snapshot.
- Make audio output default to ALSA in default config (#970).
- Trim pre-2005 %%changelog entries.

* Sat May 06 2006 Noa Resare <noa@resare.com>
- Move doc to a separate package (#960).

* Sun Apr 16 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.0-0.39.20060412
- Enable Musepack support.

* Thu Apr 13 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.0-0.38.20060412
- 2006-04-12 CVS snapshot.
- Fix 3dnow disabling patch, some parts were erroneously omitted in the
  previous revision (Thomas Jansen).

* Sat Apr  8 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.0-0.38.20060407
- 2006-04-07 CVS snapshot using shared ffmpeg, GTK2, FAAC, OpenAL, and XvMC.
- XMMS input plugin support can be disabled by rebuilding with "--without xmms"
- GUI changes: use upstream desktop entry file, update GTK icon cache and
  desktop database at post(un)install time, install icon to %%{_datadir}/icons.
- Drop lots of obsolete patches.

* Fri Mar 24 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
1.0-0.37.pre7try2
- fix #836
- fix #835,#834 by disabling detection of 3dnowext for now (Thomas Jansen)
  this should work around the garbage sound output

* Sat Mar 18 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.0-0.36.pre7try2
- Add RLO identifier to version string per upstream recommendation.
- Use configure flags instead of patch for enabling v4l*.
- Make DVB and DirectFB support unconditional.
- Drop libXvMC-devel build dependency until xvmc is actually built (#731).
- Backport get_time_pos slave mode command from CVS to fix progress bar
  with mplayerplug-in >= 3.15.
- Drop vdr-mplayer slave mode patch.
- Rename mplayer-mencoder to mencoder.

* Fri Mar 17 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
1.0-0.35.pre7try2
- fix x86_64 asm issues (maybe?!)
- fix file section for ppc

* Thu Mar 09 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- switch to new release field

* Tue Feb 28 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- add dist

* Thu Feb 23 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.0-0.lvn.0.34.pre7try2
- Apply upstream demuxer.h heap overflow fix (CVE-2006-0579).
- Fix build time X11 detection on lib64 archs.
- Update Blue skin to 1.5.

* Mon Jan 16 2006 Adrian Reber <adrian@lisas.de> - 1.0-0.lvn.0.32.pre7try2
- re-enabled the aalib-devel BR

* Thu Dec 22 2005 Ville Skyttä <ville.skytta at iki.fi> - 1.0-0.lvn.0.31.pre7try2
- Apply fix for CVE-2005-4048 from ffmpeg CVS.

* Sun Dec 11 2005 Adrian Reber <adrian@lisas.de> - 1.0-0.lvn.0.30.pre7try2
- changed BR for modular X
- temporary removal of aalib-devel BR

* Fri Nov 25 2005 Ville Skyttä <ville.skytta at iki.fi> - 1.0-0.lvn.0.29.pre7try2
- More pre-FC3 cleanups.
- Make "Blue" the default skin by symlinking, fixes fallback (#571).
- Build against new DirectFB.

* Thu Sep 29 2005 Ville Skyttä <ville.skytta at iki.fi> - 1.0-0.lvn.0.28.pre7try2
- Clean up obsolete pre-FC3 stuff (LIRC, CACA, DXR3, and Enca support now
  unconditional).
- Drop zero Epochs.

* Thu Sep 15 2005 Ville Skyttä <ville.skytta at iki.fi> - 0:1.0-0.lvn.0.27.pre7try2
- Enable Enca by default, build with it for FC3+.

* Tue Sep  6 2005 Ville Skyttä <ville.skytta at iki.fi> - 0:1.0-0.lvn.0.26.pre7try2
- 1.0pre7try2.
- Enable v4l2 interface (#576).
- Enable DVB support only with recent enough glibc-kernheaders.

* Mon Jul  4 2005 Thorsten Leemhuis <fedora at leemhuis.info> - 0:1.0-0.lvn.0.26.pre7
- Add a patch to allow compiling for x86_64-FC4; thx to Ryo Dairiki:
  https://www.redhat.com/archives/fedora-extras-list/2005-July/msg00997.html

* Mon Jul  4 2005 Ville Skyttä <ville.skytta at iki.fi> - 0:1.0-0.lvn.0.25.pre7
- Enable DirectFB by default, rebuild with "--without directfb" to disable.
- Clean up obsolete pre-FC2 support.

* Thu Jun 30 2005 Dams <anvil[AT]livna.org> - 0:1.0-0.lvn.0.24.pre7
- Added patch to fix ppc/altivec builds (#494)

* Mon Jun 20 2005 Ville Skyttä <ville.skytta at iki.fi> - 0:1.0-0.lvn.0.23.pre7
- Completely disable parallel make for now.

* Mon Jun  6 2005 Thorsten Leemhuis <fedora at leemhuis.info> - 0:1.0-0.lvn.0.22.pre7
- add gcc4 patch from thias/gentoo/myself

* Mon May  9 2005 Ville Skyttä <ville.skytta at iki.fi> - 0:1.0-0.lvn.0.21.pre7
- Use em8300-devel for DXR3 support, and make it optional, default enabled.

* Tue May 03 2005 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]info> - 0:1.0-0.lvn.0.20.pre7
- fix build issues on x86_64:
 - move target= to a ix86 section -- on x86_64 it passes the option x86-64 
   and not x86_64
 - use explicit --with-xmmslibdir
 - {_libdir}/libdha.so.* and {_libdir}/mplayer are missing on x86_64

* Tue Apr 19 2005 Dams <anvil[AT]livna.org> - 0:1.0-0.lvn.0.19.pre7
- Updated installstrip patch
- Updated ldconfig patch
- Updated to 1.0pre7

* Sun Feb 27 2005 Ville Skyttä <ville.skytta at iki.fi> 0:1.0-0.lvn.0.18.pre6a
- Fix PPC build (David Woodhouse, bug 376).
- Add libcaca support (rebuild "--without caca" to disable).
- Rebuild with LIRC support.

* Thu Jan  6 2005 Ville Skyttä <ville.skytta at iki.fi> 0:1.0-0.lvn.0.17.pre6a
- Update to 1.0pre6a (== 1.0pre6 + included HTML docs).

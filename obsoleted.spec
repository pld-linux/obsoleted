# TODO
# - handle epoch
# - hu ;)
Summary:	Obsolete packages in PLD Linux distro
Name:		obsoleted
Version:	0
Release:	23
License:	GPL
Group:		Base
BuildRequires:	rpm >= 4.4.9-56
# poldek is stupid, it does not consider noarch migration as healthy as same arch pkg
# if you wish to debug and fix, then here's trace log:
# POLDEK_TRACE=1 poldek -u ntp-client -tv -vvvvvvvv
# http://glen.alkohol.ee/pld/poldek-ntptrace.log.bz2
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# Adapter: This file does not like to be adapterized!

# rpmbuild: we have no binary payloads
%define		_enable_debug_packages	0

%description
This package sole purpose is to provide upgrade to new names of
obsoleted packages.

%define	PkgN(n:) %(NVR=%{-n*}; NV=${NVR%%-*}; N=${NV%%-*}; VR=${NVR#$N-}; V=${VR%%-*}; R=${VR#*-}; echo $N)
%define	PkgV(n:) %(NVR=%{-n*}; NV=${NVR%%-*}; N=${NV%%-*}; VR=${NVR#$N-}; V=${VR%%-*}; R=${VR#*-}; echo $V)
%define	PkgR(n:) %(NVR=%{-n*}; NV=${NVR%%-*}; N=${NV%%-*}; VR=${NVR#$N-}; V=${VR%%-*}; R=${VR#*-}; echo $R)

%define		migrate() \
%package -n %{PkgN -n %1} \
Summary:	%{PkgN -n %1} -> %{PkgN -n %3} upgrade path. \
Summary(pl.UTF-8):	Automatyczna migracja %{PkgN -n %1} -> %{PkgN -n %3}.\
Group:		Base \
Version:	%{PkgV -n %1} \
Release:	%{PkgR -n %1} \
Requires:	%{PkgN -n %3} >= %{PkgV -n %3}-%{PkgR -n %3} \
\
%description -n %{PkgN -n %1} \
%{PkgN -n %1} -> %{PkgN -n %3} upgrade path.\
\
%description -n %{PkgN -n %1} -l pl.UTF-8 \
Automatyczna migracja %{PkgN -n %1} -> %{PkgN -n %3}.\
\
%files -n %{PkgN -n %1}\
%{nil}

# NOTES about writing rules:
#
# The upgraded package MUST obsolete the version we provide, thus
# rule with "ntp-4.2.4p8-6 -> ntpd-4.2.4p8-8"
# ntpd-4.2.4p8-8 MUST "Obsolete: ntp < 4.2.4p8-6"
# and "ntp-4.2.4p8-6" must be bigger than last name of old package name, ie
# ntp-4.2.4p8-3 was last package with old name.
#
# everything else is just magic, watch and have fun :)

# Usage: migrate OLD_NAME-VERSION-RELEASE -> NEW_NAME-VERSION-RELEASE
%migrate ntp-4.2.4p8-6 -> ntpd-4.2.4p8-8
%migrate ntp-client-4.2.4p8-6 -> ntpdate-4.2.4p8-8

%migrate util-linux-ng-2.20-1 -> util-linux-2.19.1-2
%migrate util-linux-ng-chkdupexe-2.20-1 -> util-linux-chkdupexe-2.19.1-2
%migrate util-linux-ng-libs-2.20-1 -> libblkid-2.19.1-2
%migrate util-linux-ng-devel-2.20-1 -> libblkid-devel-2.19.1-2
%migrate util-linux-ng-static-2.20-1 -> libblkid-static-2.19.1-2
%migrate util-linux-ng-initrd-2.20-1 -> util-linux-initrd-2.19.1-2

%migrate vixie-cron-4.4-1 -> cronie-1.4.1-1

%migrate man-1.7-1 -> man-db-2.6.1-1

%migrate blinken-4.8.100-1 -> kde4-blinken-4.8.0-2
%migrate cantor-4.8.100-1 -> kde4-cantor-4.8.0-3
%migrate gwenview-4.8.100-1 -> kde4-gwenview-4.8.0-3
%migrate kalgebra-4.8.100-1 -> kde4-kalgebra-4.8.0-2
%migrate kalzium-4.8.100-1 -> kde4-kalzium-4.8.0-2
%migrate kamera-4.8.100-1 -> kde4-kamera-4.8.0-2
%migrate kanagram-4.8.100-1 -> kde4-kanagram-4.8.0-2
%migrate kate-4.8.100-1 -> kde4-kate-4.8.0-2
%migrate kcolorchooser-4.8.100-1 -> kde4-kcolorchooser-4.8.0-2
%migrate kde4-kdeaccessibility-jovie-4.8.100-1 -> kde4-jovie-4.8.0-2
%migrate kde4-kdebase-kwrite-4.6.99-1 -> kde4-kate-4.8.0-1
%migrate kde4-kdegraphics-gwenview-4.6.99-1 -> kde4-gwenview-4.8.0-3
%migrate kde4-kdegraphics-kamera-4.6.99-1 -> kde4-kamera-4.8.0-1
%migrate kde4-kdegraphics-kcolorchooser-4.6.99-1 -> kde4-kcolorchooser-4.8.0-1
%migrate kde4-kdegraphics-kfile-4.6.100-1 -> kde4-konqueror-4.8.0-1
%migrate kde4-kdegraphics-kgamma-4.6.99-1 -> kde4-kgamma-4.8.0-1
%migrate kde4-kdegraphics-kolourpaint-4.6.99-1 -> kde4-kolourpaint-4.8.0-1
%migrate kde4-kdegraphics-kruler-4.6.99-1 -> kde4-svgpart-4.8.0-1
%migrate kde4-kdegraphics-ksnapshot-4.6.99-1 -> kde4-ksnapshot-4.8.0-2
%migrate kde4-kdegraphics-svgpart-4.6.99-1 -> kde4-kruler-4.8.0-1
%migrate kde4-kdemultimedia-audiocd-4.8.100-1 -> kde4-audiocd-kio-4.9.0-1
%migrate kde4-kdemultimedia-cddb-4.8.100-1 -> kde4-libkcddb-4.9.0-1
%migrate kde4-kdemultimedia-dragon-4.8.100-1 -> kde4-dragon-4.9.0-1
%migrate kde4-kdemultimedia-ffmpegthumbs-4.8.100-1 -> kde4-ffmpegthumbs-4.9.0-1
%migrate kde4-kdemultimedia-juk-4.8.100-1 -> kde4-juk-4.9.0-1
%migrate kde4-kdemultimedia-kmix-4.8.100-1 -> kde4-kmix-4.9.0-1
%migrate kde4-kdemultimedia-kscd-4.8.100-1 -> kde4-kscd-4.9.0-1
%migrate kde4-kdemultimedia-libkcddb-4.8.100-1 -> kde4-libkcddb-4.9.0-1
%migrate kde4-kdemultimedia-mplayerthumbs-4.8.100-1 -> kde4-mplayerthumbs-4.9.0-1
%migrate kde4-kdesdk-kate-4.6.99-1 -> kde4-kate-4.8.0-1
%migrate kde4-kdeutils-ark-4.8.100-1 -> kde4-ark-4.8.0-1
%migrate kde4-kdeutils-filelight-4.8.100-1 -> kde4-filelight-4.8.0-1
%migrate kde4-kdeutils-kgpg-4.8.100-1 -> kde4-kgpg-4.8.0-1
%migrate kde4-kdeutils-kwalletmanager-4.8.100-1 -> kde4-kwallet-4.8.0-2
%migrate kdegraphics-strigi-analyzer-4.8.100-1 -> kde4-kdegraphics-strigi-analyzer-4.8.0-1
%migrate kdegraphics-thumbnailers-4.8.100-1 -> kde4-kdegraphics-thumbnailers-4.8.0-1
%migrate kgamma-4.8.100-1 -> kde4-kgamma-4.8.0-2
%migrate kgeography-4.8.100-1 -> kde4-kgeography-4.8.0-1
%migrate khangman-4.8.100-1 -> kde4-khangman-4.8.0-1
%migrate kig-4.8.100-1 -> kde4-kig-4.8.0-1
%migrate kimono-4.8.100-1 -> kde4-kimono-4.8.0-1
%migrate kiten-4.8.100-1 -> kde4-kiten-4.8.0-1
%migrate klettres-4.8.100-1 -> kde4-klettres-4.8.0-1
%migrate kmplot-4.8.100-1 -> kde4-kmplot-4.8.0-1
%migrate kolourpaint-4.8.100-1 -> kde4-kolourpaint-4.8.0-1
%migrate konsole-4.8.100-1 -> kde4-konsole-4.8.0-2
%migrate kruler-4.8.100-1 -> kde4-kruler-4.8.0-1
%migrate ksaneplugin-4.8.100-1 -> kde4-ksaneplugin-4.8.0-2
%migrate ksnapshot-4.8.100-1 -> kde4-ksnapshot-4.8.0-2
%migrate kstars-4.8.100-1 -> kde4-kstars-4.8.0-1
%migrate kturtle-4.8.100-1 -> kde4-kturtle-4.8.0-1
%migrate kwordquiz-4.8.100-1 -> kde4-kwordquiz-4.8.0-1
%migrate libkdcraw-4.8.100-1 -> kde4-libkdcraw-4.8.0-2
%migrate libkdeedu-4.8.100-1 -> kde4-libkdeedu-4.8.0-2
%migrate libkexiv2-4.8.100-1 -> kde4-libkexiv2-4.8.0-2
%migrate libkipi-4.8.100-1 -> kde4-libkipi-4.8.0-2
%migrate libksane-4.8.100-1 -> kde4-libksane-4.8.0-2
%migrate marble-4.8.100-1 -> kde4-marble-4.8.0-2
%migrate mobipocket-4.8.100-1 -> kde4-kdegraphics-mobipocket-4.8.0-1
%migrate okular-4.8.100-1 -> kde4-okular-4.8.0-2
%migrate parley-4.8.100-1 -> kde4-parley-4.8.0-1
%migrate qyoto-4.8.100-1 -> kde4-qyoto-4.8.0-1
%migrate rocs-4.8.100-1 -> kde4-rocs-4.8.0-1
%migrate smokegen-4.8.100-1 -> kde4-smokegen-4.8.0-1
%migrate smokekde-4.8.100-1 -> kde4-smokekde-4.8.0-1
%migrate smokeqt-4.8.100-1 -> kde4-smokeqt-4.8.0-1
%migrate step-4.8.100-1 -> kde4-step-4.8.0-1
%migrate svgpart-4.8.100-1 -> kde4-svgpart-4.8.0-2

%prep
%setup -qcT

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

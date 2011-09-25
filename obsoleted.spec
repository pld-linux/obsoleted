# TODO
# - handle epoch
# - hu ;)
Summary:	Obsolete packages in PLD Linux distro
Name:		obsoleted
Version:	0
Release:	8
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
# rule with "ntp-4.2.4p8-6 => ntpd-4.2.4p8-8"
# ntpd-4.2.4p8-8 MUST "Obsolete: ntp < 4.2.4p8-6"
# and "ntp-4.2.4p8-6" must be bigger than last name of old package name, ie
# ntp-4.2.4p8-3 was last package with old name.
#
# everything else is just magic, watch and have fun :)

# Usage: migrate OLD_NAME-VERSION-RELEASE => NEW_NAME-VERSION-RELEASE
%migrate ntp-4.2.4p8-6 => ntpd-4.2.4p8-8
%migrate ntp-client-4.2.4p8-6 => ntpdate-4.2.4p8-8
%migrate util-linux-ng-2.19-1 => util-linux-2.19.1-1
%migrate vixie-cron-4.1-24 => cronie-1.4.1-1
%migrate kde4-kdeedu-blinken-4.7.0-1 => blinken-4.7.0-1
%migrate kde4-kdeedu-cantor-4.7.0-1 => cantor-4.7.0-1
%migrate kde4-kdeedu-gwenview-4.7.0-1 => gwenview-4.7.0-1
%migrate kde4-kdeedu-kalgebra-4.7.0-1 => kalgebra-4.7.0-1
%migrate kde4-kdeedu-kalzium-4.7.0-1 => kalzium-4.7.0-1
%migrate kde4-kdeedu-kanagram-4.7.0-1 => kanagram-4.7.0-1
%migrate kde4-kdeedu-kbruch-4.7.0-1 => kbruch-4.7.0-1
%migrate kde4-kdeedu-kgeography-4.7.0-1 => kgeography-4.7.0-1
%migrate kde4-kdeedu-khangman-4.7.0-1 => khangman-4.7.0-1
%migrate kde4-kdeedu-kig-4.7.0-1 => kig-4.7.0-1
%migrate kde4-kdeedu-kiten-4.7.0-1 => kiten-4.7.0-1
%migrate kde4-kdeedu-klettres-4.7.0-1 => klettres-4.7.0-1
%migrate kde4-kdeedu-kmplot-4.7.0-1 => kmplot-4.7.0-1
%migrate kde4-kdeedu-kstars-4.6.100-1 => kstars-4.7.0-1
%migrate kde4-kdeedu-ktouch-4.6.100-1 => ktouch-4.7.0-1
%migrate kde4-kdeedu-kturtle-4.6.100-1 => kturtle-4.7.0-1
%migrate kde4-kdeedu-kwordquiz-4.6.100-1 => kwordquiz-4.7.0-1
%migrate kde4-kdeedu-marble-4.6.100-1 => marble-4.7.0-1
%migrate kde4-kdeedu-parley-4.6.100-1 => parley-4.7.0-1
%migrate kde4-kdeedu-rocs-4.6.100-1 => rocs-4.7.0-1
%migrate kde4-kdeedu-step-4.6.100-1 => step-4.7.0-1
%migrate kde4-kdegraphics-kcolorchooser-4.7.0-1 => kcolorchooser-4.7.0-1
%migrate kde4-kdegraphics-kamera-4.7.0-1 => kamera-4.7.0-1
%migrate kde4-kdegraphics-kgamma-4.7.0-1 => kgamma-4.7.0-1
%migrate kde4-kdegraphics-kgolourpaint-4.7.0-1 => kolourpaint-4.7.0-1
%migrate kde4-kdegraphics-kruler-4.6.100-1 => kolourpaint-4.7.0-1
%migrate kde4-kdegraphics-ksane-4.6.100-1 => ksane-4.7.0-1
%migrate kde4-kdegraphics-ksnapshot-4.6.100-1 => ksnapshot-4.7.0-1
%migrate kde4-kdegraphics-svgpart-4.6.100-1 => svgpart-4.7.0-1
%migrate kde4-kdegraphics-okular-4.6.100-1 => okular-4.7.0-1
%migrate kio_msits-4.6.100-1 => okular-4.7.0-1
%migrate kde4-kdebase-kwrite-4.7.0-1 => kate-4.7.0-1
%migrate kde4-kdesdk-kate-4.7.0-1 => kate-4.7.0-1
%migrate kde4-kdebindings-smoke-qt-4.7.0-1 => smokeqt-4.7.0-1
%migrate kde4-kdebindings-smoke-kde-4.7.0-1 => smokekde-4.7.0-1
%migrate kde4-kdebindings-smoke-devel-4.7.0-1 => smokegen-devel-4.7.0-1
%migrate kde4-libkdcraw-4.6.100-1 => libkdcraw-4.7.0-1
%migrate kde4-libkdeedu-4.6.100-1 => libkdeedu-4.7.0-1
%migrate kde4-kdeedu-devel-4.6.100-1 => libkdeedu-devel-4.7.0-1
%migrate kde4-kdeedu-devel-4.6.100-1 => marble-devel-4.7.0-1
%migrate kde4-libkexiv2-4.6.100-1 => libkexiv2-4.7.0-1
%migrate kde4-libkipi-4.6.100-1 => libkipi-4.7.0-1
%migrate kde4-kdegraphics-ksane-4.6.100-1 => libksane-4.7.0-1
%migrate kde4-kdegraphics-devel-4.6.100-1 => libkdcraw-devel-4.7.0-1
%migrate kde4-kdegraphics-devel-4.6.100-1 => libkexiv2-devel-4.7.0-1
%migrate kde4-kdegraphics-devel-4.6.100-1 => libkipi-devel-4.7.0-1
%migrate kde4-kdegraphics-devel-4.6.100-1 => libksane-devel-4.7.0-1
%migrate kde4-kdegraphics-devel-4.6.100-1 => okular-devel-4.7.0-1

%prep
%setup -qcT

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

# TODO
# - handle epoch
Summary:	Obsolete packages in PLD Linux distro
Name:		obsoleted
Version:	0
Release:	27
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

%migrate util-linux-ng-2.20-1 => util-linux-2.19.1-2
%migrate util-linux-ng-libs-2.20-1 => libblkid-2.19.1-2
%migrate util-linux-ng-devel-2.20-1 => libblkid-devel-2.19.1-2
%migrate util-linux-ng-static-2.20-1 => libblkid-static-2.19.1-2

%migrate vixie-cron-4.4-1 => cronie-1.4.1-1

%migrate man-1.7-1 => man-db-2.6.1-1

%prep
%setup -qcT

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

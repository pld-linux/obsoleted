# TODO
# - handle subpackages
# - handle epoch
# - pl, hu ;)
Summary:	Obsolete packages in PLD Linux distro
Name:		obsoleted
Version:	0
Release:	1
License:	GPL
Group:		Base
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package sole purpose is to provide upgrade to new names of
obsoleted packages.

%define	PkgN(n:) %(NVR=%{-n*}; IFS=-;set -- $NVR; echo $1)
%define	PkgV(n:) %(NVR=%{-n*}; IFS=-;set -- $NVR; echo $2)
%define	PkgR(n:) %(NVR=%{-n*}; IFS=-;set -- $NVR; echo $3)

%define		migrate() \
%package -n %{PkgN -n %1} \
Summary:	%{PkgN -n %1} -> %{PkgN -n %3} upgrade path \
Group:		Base \
Version:	%{PkgV -n %1} \
Release:	%{PkgR -n %1} \
Requires:	%{PkgN -n %3} >= %{PkgV -n %3}-%{PkgR -n %3} \
\
%description -n %{PkgN -n %1} \
%{PkgN -n %1} -> %{PkgN -n%3} upgrade path.\
\
%files -n %{PkgN -n %1}\
%{nil}

# NOTES about writing rules:
# The upgraded package MUST obsolete the version we provide, thus
# rule with "ntp-4.2.4p8-4 => ntpd-4.2.4p8-5"
# ntpd-4.2.4p8-5 MUST "Obsolete: ntp < 4.2.4p8-4"
# everything else is just magic, watch and have fun :)

%migrate ntp-4.2.4p8-4 => ntpd-4.2.4p8-5
%migrate ntp-client-4.2.4p8-4 => ntpdate-4.2.4p8-5

%prep
%setup -qcT

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

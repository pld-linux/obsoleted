# TODO
# - handle subpackages
# - handle epoch
# - hu ;)
Summary:	Obsolete packages in PLD Linux distro
Name:		obsoleted
Version:	0
Release:	1
License:	GPL
Group:		Base
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# Adapter: This file does not like to be adapterized!

%description
This package sole purpose is to provide upgrade to new names of
obsoleted packages.

%define	PkgN(n:) %(set -x;NVR=%{-n*}; IFS=-;set -- $NVR; V=$(eval echo \"\\$$(($#-1))\"); R=$(eval echo \"\\$$(($#-0))\"); unset IFS; echo ${NVR%%-$V-$R})
%define	PkgV(n:) %(set -x;NVR=%{-n*}; IFS=-;set -- $NVR; eval echo \"\\$$(($#-1))\")
%define	PkgR(n:) %(set -x;NVR=%{-n*}; IFS=-;set -- $NVR; eval echo \"\\$$#\")

%define		migrate() \
%package -n %{PkgN -n %1} \
Summary:	%{PkgN -n %1} -> %{PkgN -n %3} upgrade path. \
Summary(pl.UTF-8):	Automatyczna migracja %{PkgN -n %1} -> %{PkgN -n%3}.\
Group:		Base \
Version:	%{PkgV -n %1} \
Release:	%{PkgR -n %1} \
Requires:	%{PkgN -n %3} >= %{PkgV -n %3}-%{PkgR -n %3} \
\
%description -n %{PkgN -n %1} \
%{PkgN -n %1} -> %{PkgN -n%3} upgrade path.\
\
%description -n %{PkgN -n %1} -l pl.UTF-8 \
Automatyczna migracja %{PkgN -n %1} -> %{PkgN -n%3}.\
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

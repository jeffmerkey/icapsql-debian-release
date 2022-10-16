%define _build_id_links none
%define debug_package %{nil}

Name:           icapsql-debian-release
Version:        1.0
Release:        1
Summary:        ICAPSQL Debian Linux repository configuration 
License:        LGPL

URL:            http://www.icapsql.com
Source0:        icapsql.list
BuildArch:      noarch

%description
This package contains the ICAPSQL Debian Linux repository
and ICAPSQL Repository configuration for apt and apt-get.

%prep
%setup -q -c -T

%install
# apt
install -dm 755 %{buildroot}%{_sysconfdir}/apt/sources.list.d/
install -pm 644 %{SOURCE0} %{buildroot}%{_sysconfdir}/apt/sources.list.d/

%files
%config(noreplace) %{_sysconfdir}/apt/sources.list.d/icapsql.list

%changelog


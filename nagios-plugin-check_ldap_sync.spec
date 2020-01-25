%define		plugin	check_ldap_sync
Summary:	Nagios plugin to check LDAP servers are synchronization
Name:		nagios-plugin-%{plugin}
Version:	0.1
Release:	0.1
License:	GPL v2
Group:		Networking
Source0:	https://secure.opsera.com/svn/opsview/trunk/opsview-core/nagios-plugins/check_ldap_sync
# Source0-md5:	c7a95aa75b929e032319defdf605cba0
Source1:	%{plugin}.cfg
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	nagios-common
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/nagios/plugins
%define		plugindir	%{_prefix}/lib/nagios/plugins

%description
Nagios plugin to check that specified LDAP servers are synchronised.

%prep
%setup -qcT
%{__sed} -e 's,%{_prefix}/local/nagios/perl/lib,%{plugindir},' %{SOURCE0} > %{plugin}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{plugindir}}
install -p %{plugin} $RPM_BUILD_ROOT%{plugindir}/%{plugin}
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/%{plugin}.cfg

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(640,root,nagios) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{plugin}.cfg
%attr(755,root,root) %{plugindir}/%{plugin}

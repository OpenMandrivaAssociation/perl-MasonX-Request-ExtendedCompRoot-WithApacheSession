%define upstream_name    MasonX-Request-ExtendedCompRoot-WithApacheSession
%define upstream_version 0.03

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Extend functionality of Mason's comp_root and add a session to the Mason Request object
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/dists/%{upstream_name}-%{upstream_version}.tar.bz2 

BuildRequires:	perl(MasonX::Request::ExtendedCompRoot)
BuildRequires:	perl(MasonX::Request::WithApacheSession)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This  module simply integrates "MasonX::Request::ExtendedCompRoot"
and "MasonX::Request::WithApacheSession".

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor 
%{__make}

%check
%__make test

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes LICENSE README
%{perl_vendorlib}/MasonX/Request/ExtendedCompRoot/WithApacheSession.pm
%{_mandir}/man3/*

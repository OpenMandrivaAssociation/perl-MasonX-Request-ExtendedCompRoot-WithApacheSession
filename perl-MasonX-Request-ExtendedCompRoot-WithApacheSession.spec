%define realname MasonX-Request-ExtendedCompRoot-WithApacheSession

Summary:	Extend functionality of Mason's comp_root and add a session to the Mason Request object
Name:           perl-%{realname}
Version:        0.03
Release:        %mkrel 2
License:	GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{realname}
Source0:	http://search.cpan.org/dists/%{realname}-%{version}.tar.bz2 
BuildRequires:	perl(MasonX::Request::ExtendedCompRoot)
BuildRequires:	perl(MasonX::Request::WithApacheSession)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
This  module simply integrates "MasonX::Request::ExtendedCompRoot"
and "MasonX::Request::WithApacheSession".

%prep

%setup -q -n %{realname}-%{version}

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


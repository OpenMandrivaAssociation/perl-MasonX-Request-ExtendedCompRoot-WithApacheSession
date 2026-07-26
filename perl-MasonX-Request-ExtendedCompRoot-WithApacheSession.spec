%define upstream_name    MasonX-Request-ExtendedCompRoot-WithApacheSession
Name:		perl-%{upstream_name}
Version:	0.04
Release:	2

Summary:	Integrates MasonX::Request ::ExtendedCompRoot and ::WithApacheSession
License:	GPL
Group:		Development/Perl
Url:		https://metacpan.org/dist/MasonX-Request-ExtendedCompRoot-WithApacheSession
Source0:	https://cpan.metacpan.org/authors/id/S/SG/SGP/MasonX-Request-ExtendedCompRoot-WithApacheSession-%{version}.tar.gz 

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(MasonX::Request::ExtendedCompRoot)
BuildRequires:	perl(MasonX::Request::WithApacheSession)
BuildArch:	noarch

%description
Extend functionality of Mason's comp_root and add a session to
the Mason Request object.

This  module simply integrates "MasonX::Request::ExtendedCompRoot"
and "MasonX::Request::WithApacheSession".

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor 
make

%check
make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{perl_vendorlib}/MasonX/Request/ExtendedCompRoot/WithApacheSession.pm
%{_mandir}/man3/*


%changelog
* Sat Aug 01 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.30.0-1mdv2010.0
+ Revision: 405914
- rebuild using %0.04 Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.03-4mdv2009.0
+ Revision: 241723
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Wed May 03 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.03-2mdk
- Fix According to perl Policy
	- Source URL
	- BuildRequires

* Fri Jan 27 2006 Oden Eriksson <oeriksson@mandriva.com> 0.03-1mdk
- initial Mandriva package


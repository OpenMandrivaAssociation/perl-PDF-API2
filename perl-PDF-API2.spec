%define module  PDF-API2
%define name    perl-%{module}
%define version 0.65
%define release %mkrel 1

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        PDF-API2 Perl module
License:        Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/PDF/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
BuildRequires:  perl(Compress::Zlib)
Buildarch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
This module is 'The Next Generation' of Text::PDF::API which initially 
provided a nice API around the Text::PDF::* modules created by Martin Hosken.

%prep
%setup -q  -n %{module}-%{version}
find contrib -type f | xargs perl -pi -e 's|^#!/usr/local/bin/perl|#!/usr/bin/perl|' 
perl -pi -e 'tr/\r//d' CHANGELOG LICENSE contrib/pdf-deoptimize.pl

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor MAN1PODS='' MAN3PODS=''
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std
rm -f %{buildroot}%{perl_vendorlib}/PDF/API2/Win32.pm
rm -f %{buildroot}%{perl_vendorlib}/PDF/API2/Basic/TTF/Win32.pm

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc AUTHORS CONTACT COPYING INSTALL LICENSE README TODO VERSION contrib examples
%{perl_vendorlib}/PDF
%{_mandir}/*/*

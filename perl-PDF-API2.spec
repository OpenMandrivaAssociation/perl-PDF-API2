%define upstream_name    PDF-API2
%define upstream_version 2.018

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    PDF-API2 Perl module
License:    Artistic
Group:      Development/Perl
URL:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/PDF/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(Font::TTF::Font)
Buildarch:      noarch
Requires:       fonts-ttf-dejavu
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
This module is 'The Next Generation' of Text::PDF::API which initially 
provided a nice API around the Text::PDF::* modules created by Martin Hosken.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
find contrib -type f | xargs \
    perl -pi -e 's|^#!/usr/local/bin/perl|#!/usr/bin/perl|' 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std
rm -f %{buildroot}%{perl_vendorlib}/PDF/API2/Win32.pm
rm -f %{buildroot}%{perl_vendorlib}/PDF/API2/Basic/TTF/Win32.pm
rm -rf %{buildroot}%{perl_vendorlib}/PDF/API2/fonts

install -d -m 755 %{buildroot}%{_bindir}
install -m 755 contrib/* %{buildroot}%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc Changes CONTACT HACKING LICENSE PATENTS README examples
%{perl_vendorlib}/PDF
%{_mandir}/*/*
%{_bindir}/*

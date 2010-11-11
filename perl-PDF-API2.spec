%define upstream_name    PDF-API2
%define upstream_version 0.73

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 3

Summary:    PDF-API2 Perl module
License:    Artistic
Group:      Development/Perl
URL:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/PDF/%{upstream_name}-%{upstream_version}.tar.gz
Patch0:     %{name}-0.73-man-pages.patch
Patch1:     %{name}-0.73-fix-program-output.patch

BuildRequires:  perl(Compress::Zlib)
Buildarch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
Requires:       fonts-ttf-dejavu

%description
This module is 'The Next Generation' of Text::PDF::API which initially 
provided a nice API around the Text::PDF::* modules created by Martin Hosken.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
%patch0 -p 1
%patch1 -p 1
find contrib -type f | xargs \
    perl -pi -e 's|^#!/usr/local/bin/perl|#!/usr/bin/perl|' 

# fix the permissions of the files that will be doc'ed
chmod 644 AUTHORS CONTACT COPYING INSTALL LICENSE README TODO VERSION examples/*

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
%doc AUTHORS CONTACT COPYING INSTALL LICENSE README TODO VERSION examples
%{perl_vendorlib}/PDF
%{_mandir}/*/*
%{_bindir}/*

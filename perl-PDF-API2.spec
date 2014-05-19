%define upstream_name    PDF-API2%define upstream_version 2.021

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	PDF-API2 Perl module
License:	Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/PDF/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	 perl-devel
BuildRequires:	 perl(Compress::Zlib)
BuildRequires:	 perl(Font::TTF::Font)
BuildArch:	noarch
Requires:	fonts-ttf-dejavu

%description
This module is 'The Next Generation' of Text::PDF::API which initially 
provided a nice API around the Text::PDF::* modules created by Martin Hosken.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
find contrib -type f | xargs \
    perl -pi -e 's|^#!/usr/local/bin/perl|#!/usr/bin/perl|' 

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std
rm -f %{buildroot}%{perl_vendorlib}/PDF/API2/Win32.pm
rm -f %{buildroot}%{perl_vendorlib}/PDF/API2/Basic/TTF/Win32.pm
rm -rf %{buildroot}%{perl_vendorlib}/PDF/API2/fonts

install -d -m 755 %{buildroot}%{_bindir}
install -m 755 contrib/* %{buildroot}%{_bindir}

%files
%doc Changes  LICENSE PATENTS README examples
%{perl_vendorlib}/PDF
%{_mandir}/*/*
%{_bindir}/*
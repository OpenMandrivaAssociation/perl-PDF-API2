%define upstream_name    PDF-API2
%define upstream_version 2.019

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

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
%doc Changes CONTACT HACKING LICENSE PATENTS README examples
%{perl_vendorlib}/PDF
%{_mandir}/*/*
%{_bindir}/*

%changelog
* Mon Mar 14 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.19.0-1mdv2011.0
+ Revision: 644794
- update to new version 2.019

* Thu Mar 10 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.18.0-1
+ Revision: 643433
- new version

* Sat Feb 05 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.16.0-1
+ Revision: 636163
- new version
- drop man pages installation patch, uneeded anymore

* Thu Nov 11 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.730.0-3mdv2011.0
+ Revision: 596118
- fix pdf-merge output (bug #61563)
- install contrib programs in binary directory, not at examples

* Sat Nov 06 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.730.0-2mdv2011.0
+ Revision: 594249
- fix the permissions of the docs

* Wed Jul 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.730.0-1mdv2011.0
+ Revision: 404288
- rebuild using %%perl_convert_version

* Thu May 07 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.73-1mdv2010.0
+ Revision: 373005
- new version

* Sun Nov 23 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.72.003-1mdv2009.1
+ Revision: 305981
- update to new version 0.72.003

* Tue Aug 12 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.71.001-1mdv2009.0
+ Revision: 271034
- update to new version 0.71.001

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.69-3mdv2009.0
+ Revision: 268669
- rebuild early 2009.0 package (before pixel changes)

* Sat May 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.69-2mdv2009.0
+ Revision: 208454
- don't ship dejavu fonts, juste requires them

* Tue Jan 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.69-1mdv2008.1
+ Revision: 156681
- fix build

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Nov 17 2007 Funda Wang <fwang@mandriva.org> 0.68-1mdv2008.1
+ Revision: 109366
- update to new version 0.68

* Sun Nov 04 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.66-1mdv2008.1
+ Revision: 105897
- update to new version 0.66

* Fri Oct 12 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.65-1mdv2008.1
+ Revision: 97558
- update to new version 0.65

* Thu Aug 30 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.63-1mdv2008.0
+ Revision: 75230
- update to new version 0.63

* Wed Aug 15 2007 Funda Wang <fwang@mandriva.org> 0.62-2mdv2008.0
+ Revision: 63666
- remove Win32 files

* Wed Aug 08 2007 Funda Wang <fwang@mandriva.org> 0.62-1mdv2008.0
+ Revision: 60470
- fix doc files
- New version 0.62

* Thu May 10 2007 Olivier Thauvin <nanardon@mandriva.org> 0.61-1mdv2008.0
+ Revision: 25829
- 0.61

* Thu May 03 2007 Olivier Thauvin <nanardon@mandriva.org> 0.60-1mdv2008.0
+ Revision: 22085
- 0.60


* Mon Aug 28 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.55-1mdv2007.0
- New version 0.55

* Wed Jun 21 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.53-1mdv2007.0
- New version 0.53

* Fri Jun 16 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.52-1mdv2007.0
- New version 0.52

* Mon Dec 19 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.51-1mdk
- New release 0.51
- drop patch, a command-line switch is easier to maintain

* Tue Oct 04 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.46.003-1mdk
- New release 0.46.003

* Fri Sep 30 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.46.002-2mdk
- buildrequires fix

* Fri Sep 30 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.46.002-1mdk
- New release 0.46.002

* Wed Sep 28 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.46.001-1mdk
- New release 0.46.001

* Fri Sep 23 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.46-1mdk
- new version
- rpmbuildupdate aware
- spec cleanup
- fix directory ownership
- enable tests
- better url
- fix doc files list
- force man page generation
- fix some perms and encoding

* Mon Mar 01 2004 Michael Scherer <misc@mandrake.org> 0.3r77-2mdk 
- remove useless Requires on win32

* Tue Feb 17 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.3r77-1mdk
- 0.3r77


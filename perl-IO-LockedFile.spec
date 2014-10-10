%define upstream_name    IO-LockedFile
%define upstream_version 0.23

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Supply object methods for locking files
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
In its simplistic use, the IO::LockedFile class gives us the same interface of
the IO::File class with the unique difference that the files we deal with are
locked using the Flock mechanism (using the flock function).

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes
%{_mandir}/*/*
%{perl_vendorlib}/IO/*


%changelog
* Mon Aug 03 2009 Jérôme Quelin <jquelin@mandriva.org> 0.230.0-1mdv2010.0
+ Revision: 407786
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.23-4mdv2009.0
+ Revision: 257315
- rebuild

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 0.23-2mdv2008.1
+ Revision: 135856
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.23-2mdv2008.0
+ Revision: 86508
- rebuild


* Fri Mar 24 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.23-1mdk
- First Mandriva release


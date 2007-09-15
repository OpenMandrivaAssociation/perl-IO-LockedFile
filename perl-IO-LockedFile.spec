%define realname IO-LockedFile
%define name	perl-%{realname}
%define version	0.23
%define release	%mkrel 2

Summary:	Supply object methods for locking files
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{realname}/
Source:		%{realname}-%{version}.tar.bz2
Buildroot:	%{_tmppath}/%{name}-root
BuildArch:	noarch

%description
In its simplistic use, the IO::LockedFile class gives us the same interface of
the IO::File class with the unique difference that the files we deal with are
locked using the Flock mechanism (using the flock function).

%prep
%setup -q -n %{realname}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/*/*
%{perl_vendorlib}/IO/*

%clean
rm -rf $RPM_BUILD_ROOT


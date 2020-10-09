#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	TAP
%define		pnam	Formatter-JUnit
Summary:	TAP::Formatter::JUnit - Harness output delegate for JUnit output
Summary(pl.UTF-8):	TAP::Formatter::Junit - moduł TAP Test Harness tworzący wyjście JUnit
Name:		perl-TAP-Formatter-JUnit
Version:	0.11
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/TAP/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	acdae8535ee116c13f7576b34cebb775
URL:		https://metacpan.org/release/TAP-Formatter-JUnit
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl(TAP::Harness) >= 3.12
BuildRequires:	perl-File-Slurp
BuildRequires:	perl-IO-stringy
BuildRequires:	perl-IPC-Run
BuildRequires:	perl-Moose
BuildRequires:	perl-MooseX-NonMoose
BuildRequires:	perl-Test-XML
BuildRequires:	perl-XML-Generator
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TAP::Formatter::JUnit provides JUnit output formatting for
TAP::Harness.

%description -l pl.UTF-8
TAP::Formatter::JUnit zapewnia formatowanie wyjścia JUnit dla modułu
TAP::Harness.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/tap2junit
%{perl_vendorlib}/TAP/Formatter/JUnit.pm
%{perl_vendorlib}/TAP/Formatter/JUnit
%{_mandir}/man1/tap2junit.1p*
%{_mandir}/man3/TAP::Formatter::JUnit*.3pm*

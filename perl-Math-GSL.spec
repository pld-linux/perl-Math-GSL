#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	Math
%define		pnam	GSL
Summary:	Math::GSL Perl module - resticted interface to GNU Scientific Library
Summary(pl.UTF-8):	Moduł Perla Math::GSL - ograniczony interfejs do GNU Scientific Library
Name:		perl-Math-GSL
Version:	0.44
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/Math/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c3249e41b1c304a8fb45e6982543c408
Patch0:		gsl-2.8.patch
Patch1:		Math-GSL-swig-only-curversion.patch
Patch2:		Math-GSL-test.patch
Patch3:		types.patch
URL:		https://metacpan.org/dist/Math-GSL
BuildRequires:	gsl-devel >= 1.15
BuildRequires:	perl-Alien-GSL
BuildRequires:	perl-Module-Build >= 0.38
BuildRequires:	perl-PkgConfig >= 0.07720
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
BuildRequires:	swig-perl
%if %{with tests}
BuildRequires:	perl-Test-Class >= 0.12
BuildRequires:	perl-Test-Deep
BuildRequires:	perl-Test-Differences
BuildRequires:	perl-Test-Exception >= 0.21
BuildRequires:	perl-Test-Most >= 0.31
BuildRequires:	perl-Test-Taint >= 1.06
BuildRequires:	perl-Test-Warn
BuildRequires:	perl-version >= 0.77
%endif
Requires:	gsl >= 1.15
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math::GSL Perl module is a very resticted perl interface to -lgsl -
GNU Scientific Library. Only the routines relating the solving of
polynomials are exported. It exists to provide that function to
"tkscope" in Audio::Data.

%description -l pl.UTF-8
Moduł Perla Math::GSL stanowi bardzo ograniczony interfejs do -lgsl -
Biblioteki Naukowej GNU (GNU Scientific Library). Eksportuje jedynie
funkcje dotyczące rozwiązywania równań wielomianowych. Istnieje, aby
udostępnić te funkcje "tkscope" w module Audio::Data.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1

# simulate non-release to force swig rebuild
mkdir .git

%build
export CC_FLAGS="%{rpmcppflags} %{rpmcflags}"
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
%doc CREDITS Changes KNOWN_BUGS README.md TODO
%{perl_vendorarch}/Math/GSL.pm
%{perl_vendorarch}/Math/GSL
%dir %{perl_vendorarch}/auto/Math/GSL
%dir %{perl_vendorarch}/auto/Math/GSL/*
%attr(755,root,root) %{perl_vendorarch}/auto/Math/GSL/*/*.so
%{_mandir}/man3/Math::GSL*.3pm*

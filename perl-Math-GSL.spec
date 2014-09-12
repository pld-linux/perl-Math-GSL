#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Math
%define		pnam	GSL
Summary:	Math::GSL Perl module - resticted interface to GNU Scientific Library
Summary(pl.UTF-8):	Moduł Perla Math::GSL - ograniczony interfejs do GNU Scientific Library
Name:		perl-Math-GSL
Version:	0.01
Release:	6
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Math/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	abc4474bbbf5439b46a551284013cb35
URL:		http://search.cpan.org/dist/Math-GSL/
BuildRequires:	gsl-devel
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
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

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorarch}/Math/*
%dir %{perl_vendorarch}/auto/Math/GSL
%attr(755,root,root) %{perl_vendorarch}/auto/Math/GSL/*.so

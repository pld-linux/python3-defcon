#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests

Summary:	Set of flexible objects for representing UFO data
Summary(pl.UTF-8):	Zbiór elastycznych obiektów reprezentujących dane UFO
Name:		python3-defcon
Version:	0.9.0
Release:	3
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/defcon/
Source0:	https://files.pythonhosted.org/packages/source/d/defcon/defcon-%{version}.zip
# Source0-md5:	7d725879cb9529b04e7f212d56b8f731
URL:		https://pypi.org/project/defcon/
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools >= 1:42
BuildRequires:	python3-setuptools_scm
%if %{with tests}
BuildRequires:	python3-fonttools >= 4.10.0
BuildRequires:	python3-fs >= 2.2.0
BuildRequires:	python3-pytest >= 3.0.3
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	sphinx-pdg-3
%endif
BuildRequires:	unzip
Requires:	python3-modules >= 1:3.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Defcon is a set of UFO based objects optimized for use in font editing
applications. The objects are built to be lightweight, fast and
flexible. The objects are very bare-bones and they are not meant to be
end-all, be-all objects. Rather, they are meant to provide base
functionality so that you can focus on your application's behavior,
not object observing or maintaining cached data. Defcon implements
UFO3 as described by the UFO font format
<http://unifiedfontobject.org/>.

%description -l pl.UTF-8
Defcon to zbiór opartych na UFO obiektów zoptymalizowanych do używania
w aplikacjach modyfikujących fonty. Obiekty są zbudowane jako lekkie,
szybkie i elastyczne. Są bardzo podstawowe, nie mają służyć do
wszystkiego naraz. Mają raczej udostępniać podstawową funkcjonalność,
dzięki czemu można skupić się na zachowaniu aplikacji, a nie
obserwowaniu obiektów czy utrzymywaniu danych podręcznych. Defcon ma
zaimplementowane UFO3, opisane w formacie fontów UFO:
<http://unifiedfontobject.org/>.

%package apidocs
Summary:	API documentation for Python defcon module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona defcon
Group:		Documentation

%description apidocs
API documentation for Python defcon module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona defcon.

%prep
%setup -q -n defcon-%{version}

%build
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest Lib/defcon
%endif

%if %{with doc}
%{__make} -C documentation html \
	SPHINXBUILD=sphinx-build-3
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc License.txt README.rst
%{py3_sitescriptdir}/defcon
%{py3_sitescriptdir}/defcon-%{version}-py*.egg-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc documentation/build/html/{_static,concepts,objects,*.html,*.js}
%endif

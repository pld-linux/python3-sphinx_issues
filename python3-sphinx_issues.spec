#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	Sphinx extension for linking to your project's issue tracker
Summary(pl.UTF-8):	Rozszerzenie Sphinksa do dowiązań do systemu śledzenia problemów projektu
Name:		python3-sphinx_issues
Version:	5.0.1
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0-Download: https://pypi.org/simple/sphinx-issues/
Source0:	https://files.pythonhosted.org/packages/source/s/sphinx-issues/sphinx_issues-%{version}.tar.gz
# Source0-md5:	1c258ed2f810fd43b2ab4b1825d97c35
URL:		https://github.com/sloria/sphinx-issues
BuildRequires:	python3-build
BuildRequires:	python3-flit_core < 4
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.9
%if %{with tests}
BuildRequires:	python3-Sphinx
BuildRequires:	python3-pytest >= 6.2.0
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.9
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Sphinx extension for linking to your project's issue tracker.
Includes roles for linking to both issues and user profiles, with
built-in support for GitHub (though this works with other services).

%description -l pl.UTF-8
Rozszerzenie Sphinksa służące do dowiązywania do systemu śledzenia
problemów projektu. Zawiera role do dowiązywania zarówno do zgłoszeń
problemów, jak i profili użytkowników; ma wbudowaną obsługę serwisu
GitHub (ale działa także z innymi serwisami).

%prep
%setup -q -n sphinx_issues-%{version}

%build
%py3_build_pyproject

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTHONPATH=$(pwd)/src \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/sphinx_issues
%{py3_sitescriptdir}/sphinx_issues-%{version}.dist-info

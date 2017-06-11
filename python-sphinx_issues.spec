#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Sphinx extension for linking to your project's issue tracker
Summary(pl.UTF-8):	Rozszerzenie Sphinksa do dowiązań do systemu śledzenia problemów projektu
Name:		python-sphinx_issues
Version:	0.3.1
Release:	1
License:	MIT
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/s/sphinx-issues/sphinx-issues-%{version}.tar.gz
# Source0-md5:	f0903a1b071fb8d19c434e36f8eac3dc
URL:		https://github.com/sloria/sphinx-issues
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.3
BuildRequires:	python3-setuptools
%endif
Requires:	python-modules >= 1:2.7
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

%package -n python3-sphinx_issues
Summary:	Sphinx extension for linking to your project's issue tracker
Summary(pl.UTF-8):	Rozszerzenie Sphinksa do dowiązań do systemu śledzenia problemów projektu
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.3

%description -n python3-sphinx_issues
A Sphinx extension for linking to your project's issue tracker.
Includes roles for linking to both issues and user profiles, with
built-in support for GitHub (though this works with other services).

%description -n python3-sphinx_issues -l pl.UTF-8
Rozszerzenie Sphinksa służące do dowiązywania do systemu śledzenia
problemów projektu. Zawiera role do dowiązywania zarówno do zgłoszeń
problemów, jak i profili użytkowników; ma wbudowaną obsługę serwisu
GitHub (ale działa także z innymi serwisami).

%prep
%setup -q -n sphinx-issues-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py_sitescriptdir}/sphinx_issues.py[co]
%{py_sitescriptdir}/sphinx_issues-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-sphinx_issues
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/sphinx_issues.py
%{py3_sitescriptdir}/__pycache__/sphinx_issues.cpython-*.py[co]
%{py3_sitescriptdir}/sphinx_issues-%{version}-py*.egg-info
%endif

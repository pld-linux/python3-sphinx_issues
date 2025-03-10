#
# Conditional build:
%bcond_with	tests	# unit tests [not included in sdist]

Summary:	Sphinx extension for linking to your project's issue tracker
Summary(pl.UTF-8):	Rozszerzenie Sphinksa do dowiązań do systemu śledzenia problemów projektu
Name:		python3-sphinx_issues
Version:	3.0.1
Release:	2
License:	MIT
Group:		Libraries/Python
#Source0-Download: https://pypi.org/simple/sphinx-issues/
Source0:	https://files.pythonhosted.org/packages/source/s/sphinx-issues/sphinx-issues-%{version}.tar.gz
# Source0-md5:	e2351ac5790c84b8fe9f13da294f69f1
URL:		https://github.com/sloria/sphinx-issues
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pytest >= 6.2.0
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.6
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
%setup -q -n sphinx-issues-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/sphinx_issues.py
%{py3_sitescriptdir}/__pycache__/sphinx_issues.cpython-*.py[co]
%{py3_sitescriptdir}/sphinx_issues-%{version}-py*.egg-info

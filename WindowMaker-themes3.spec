Summary:	Pack of themes for WindowMaker
Summary(pl):	Zestaw motywów dla WindowMakera
Name:		WindowMaker-themes-pack3
Version:	1.0
Release:	2
License:	GPL
Group:		Themes
Source0:	http://ep09.pld-linux.org/~havner/%{name}.tar.bz2
# Source0-md5:	cf626eabeebc5cba45cb50b0765ff511
Requires:	WindowMaker
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_themesdir	%{_datadir}/WindowMaker/Themes

%description
This is a set of various themes for WindowMaker.

%description -l pl
Zestaw ró¿nych motywów dla WindowMakera.

%prep
%setup -q -n %{name}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_themesdir}

cp -R * $RPM_BUILD_ROOT%{_themesdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_themesdir}/*

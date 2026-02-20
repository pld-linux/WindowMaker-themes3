Summary:	Pack of themes for WindowMaker
Summary(pl.UTF-8):	Zestaw motywów dla WindowMakera
Name:		WindowMaker-themes3
Version:	1.0
Release:	6
License:	GPL
Group:		Themes
Source0:	%{name}.tar.bz2
# Source0-md5:	081a76b7d4397587d44cf71b72afbbbd
Requires:	WindowMaker
Obsoletes:	WindowMaker-themes-pack3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_themesdir	%{_datadir}/WindowMaker/Themes

%description
This is a set of various themes for WindowMaker.

%description -l pl.UTF-8
Zestaw różnych motywów dla WindowMakera.

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

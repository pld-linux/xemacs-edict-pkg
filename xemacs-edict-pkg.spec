Summary:	Lisp Interface to EDICT, Kanji Dictionary
Summary(pl):	Lisp Interface to EDICT, Kanji Dictionary
Name:		xemacs-edict-pkg
%define 	srcname	edict
Version:	1.09
Release:	1
License:	GPL
Group:		Applications/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Source0:	ftp://ftp.xemacs.org/packages/%{srcname}-%{version}-pkg.tar.gz
URL:		http://www.xemacs.org/
BuildArch:	noarch
Conflicts:	xemacs-sumo
Requires:	xemacs
Requires:	xemacs-mule-base-pkg
Requires:	xemacs-base-pkg
BuildRoot:	/tmp/%{name}-%{version}-root

%description


%description -l pl 


%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

cp -a * $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

gzip -9nf lisp/edict/ChangeLog 

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc lisp/edict/ChangeLog.gz 
%dir %{_datadir}/xemacs-packages/lisp/*
%{_datadir}/xemacs-packages/lisp/*/*.elc

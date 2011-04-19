%define		plugin	hashchange
Summary:	jQuery hashchange event
Name:		jquery-%{plugin}
Version:	1.3
Release:	1
License:	MIT / GPL
Group:		Applications/WWW
Source0:	http://github.com/cowboy/jquery-hashchange/raw/v1.3/jquery.ba-hashchange.min.js
# Source0-md5:	757898a5793d29189e52ca6ee8fce808
URL:		http://benalman.com/projects/jquery-hashchange-plugin/
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	js
BuildRequires:	yuicompressor
Requires:	jquery
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/jquery/%{plugin}

%description
This jQuery plugin enables very basic bookmarkable #hash history via a
cross-browser HTML5 window.onhashchange event.

While this functionality was initially tied to the jQuery BBQ plugin,
the event.special window.onhashchange functionality has now been
broken out into a separate plugin for users who want just the basic
event & back button support, without all the extra awesomeness that
BBQ provides.

%prep
%setup -qcT
cp -p %{SOURCE0} %{plugin}.js

%build
# compress .js
install -d build
yuicompressor --charset UTF-8 %{plugin}.js -o build/%{plugin}.js
js -C -f build/%{plugin}.js

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}
cp -p build/%{plugin}.js $RPM_BUILD_ROOT%{_appdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_appdir}

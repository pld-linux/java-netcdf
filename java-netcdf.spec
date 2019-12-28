# TODO: remove (at least some) external packages from jars and use system ones
Summary:	NetCDF Java libraries
Summary(pl.UTF-8):	Biblioteki NetCDF dla języka Java
Name:		java-netcdf
Version:	4.6.14
Release:	1
License:	BSD-like
Group:		Libraries
Source0:	ftp://ftp.unidata.ucar.edu/pub/netcdf/netcdf-java/v4.6/ncIdv-%{version}.jar
# Source0-md5:	25d336beb248628922d238b79d28ab5e
Source1:	ftp://ftp.unidata.ucar.edu/pub/netcdf/netcdf-java/v4.6/netcdfAll-%{version}.jar
# Source1-md5:	9c25be54f379cf5c7f7bb047c30c7147
Source2:	ftp://ftp.unidata.ucar.edu/pub/netcdf/netcdf-java/v4.6/toolsUI-%{version}.jar
# Source2-md5:	fb99d6604f40a5201769f21a09ee9df8
URL:		http://www.unidata.ucar.edu/software/netcdf-java/
Requires:	jre
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The NetCDF Java library implements the Common Data Model (CDM) to
interface netCDF files and other types of scientific data formats.

%description -l pl.UTF-8
Biblioteka NetCDF Java implementuje model danych CDM (Common Data
Model) pozwalający na pracę z plikami netCDF i innymi rodzajami
formatów danych naukowych.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

cp -p %{SOURCE0} %{SOURCE1} %{SOURCE2} $RPM_BUILD_ROOT%{_javadir}
for f in ncIdv netcdfAll toolsUI ; do
	ln -sf ${f}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/${f}.jar
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_javadir}/ncIdv-%{version}.jar
%{_javadir}/ncIdv.jar
%{_javadir}/netcdfAll-%{version}.jar
%{_javadir}/netcdfAll.jar
%{_javadir}/toolsUI-%{version}.jar
%{_javadir}/toolsUI.jar

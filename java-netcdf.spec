# TODO: remove (at least some) external packages from jars and use system ones
Summary:	NetCDF Java libraries
Summary(pl.UTF-8):	Biblioteki NetCDF dla języka Java
Name:		java-netcdf
Version:	4.6.1
Release:	1
License:	BSD-like
Group:		Libraries
Source0:	ftp://ftp.unidata.ucar.edu/pub/netcdf/netcdf-java/v4.6/ncIdv-%{version}.jar
# Source0-md5:	aaa0ccf3c4d16dd06ddc208bc729f487
Source1:	ftp://ftp.unidata.ucar.edu/pub/netcdf/netcdf-java/v4.6/netcdfAll-%{version}.jar
# Source1-md5:	c3917863f01d7e1f4a237e90bd930995
Source2:	ftp://ftp.unidata.ucar.edu/pub/netcdf/netcdf-java/v4.6/toolsUI-%{version}.jar
# Source2-md5:	e8522134c5af381a3d78566b7ba9daa9
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

//////////////////////////////////////////////////////////////////////////
//
//  Copyright (c) 2007-2012, Image Engine Design Inc. All rights reserved.
//
//  Redistribution and use in source and binary forms, with or without
//  modification, are permitted provided that the following conditions are
//  met:
//
//     * Redistributions of source code must retain the above copyright
//       notice, this list of conditions and the following disclaimer.
//
//     * Redistributions in binary form must reproduce the above copyright
//       notice, this list of conditions and the following disclaimer in the
//       documentation and/or other materials provided with the distribution.
//
//     * Neither the name of Image Engine Design nor the names of any
//       other contributors to this software may be used to endorse or
//       promote products derived from this software without specific prior
//       written permission.
//
//  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
//  IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
//  THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
//  PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
//  CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
//  EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
//  PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
//  PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
//  LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
//  NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
//  SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
//
//////////////////////////////////////////////////////////////////////////

#ifndef IE_CORERI_TYPEIDS_H
#define IE_CORERI_TYPEIDS_H

/// The IECoreRI namespace holds all the functionality implemented in libIECoreRI
namespace IECoreRI
{

enum TypeId
{
	PTCParticleReaderTypeId = 106000,
	PTCParticleWriterTypeId = 106001,
	RendererTypeId = 106002,
	RIBWriterTypeId = 106003,
	SLOReaderTypeId = 106004,
	SXRendererTypeId = 106005,
	DTEXDeepImageReaderTypeId = 106006, // obsolete - available for reuse
	DTEXDeepImageWriterTypeId = 106007, // obsolete - available for reuse
	SHWDeepImageReaderTypeId = 106008, // obsolete - available for reuse
	SHWDeepImageWriterTypeId = 106009, // obsolete - available for reuse

	/// If we ever get here we should start over again
	LastCoreRITypeId = 106999,
};

} // namespace IECoreRI

#endif // IE_CORERI_TYPEIDS_H

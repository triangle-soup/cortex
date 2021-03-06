##########################################################################
#
#  Copyright (c) 2007-2010, Image Engine Design Inc. All rights reserved.
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are
#  met:
#
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#
#     * Neither the name of Image Engine Design nor the names of any
#       other contributors to this software may be used to endorse or
#       promote products derived from this software without specific prior
#       written permission.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
#  IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
#  THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
#  PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
#  CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
#  EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
#  PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
#  PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
#  LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
#  NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#  SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
##########################################################################

import os
import unittest
import IECore
import random

class TestPerlinNoise( unittest.TestCase ) :

	def testff( self ) :

		expected = (
			0.50000, 0.50000, 0.50000, 0.50000, 0.50000, 0.50000, 0.50000, 0.50000, 0.50000, 0.50000,
			0.50249, 0.50249, 0.50249, 0.50249, 0.50249, 0.50249, 0.50249, 0.50249, 0.50249, 0.50249,
			0.50501, 0.50501, 0.50501, 0.50501, 0.50501, 0.50501, 0.50501, 0.50501, 0.50501, 0.50501,
			0.50758, 0.50758, 0.50758, 0.50758, 0.50758, 0.50758, 0.50758, 0.50758, 0.50758, 0.50758,
			0.51020, 0.51020, 0.51020, 0.51020, 0.51020, 0.51020, 0.51020, 0.51020, 0.51020, 0.51020,
			0.51288, 0.51288, 0.51288, 0.51288, 0.51288, 0.51288, 0.51288, 0.51288, 0.51288, 0.51288,
			0.51562, 0.51562, 0.51562, 0.51562, 0.51562, 0.51562, 0.51562, 0.51562, 0.51562, 0.51562,
			0.51839, 0.51839, 0.51839, 0.51839, 0.51839, 0.51839, 0.51839, 0.51839, 0.51839, 0.51839,
			0.52119, 0.52119, 0.52119, 0.52119, 0.52119, 0.52119, 0.52119, 0.52119, 0.52119, 0.52119,
			0.52399, 0.52399, 0.52399, 0.52399, 0.52399, 0.52399, 0.52399, 0.52399, 0.52399, 0.52399,
		)

		n = IECore.PerlinNoiseff()

		width = 10
		height = 10

		for i in range( 0, height ) :
			v = 0.5 + n.noise( i/50.0 )
			for j in range( 0, width ) :
				self.assertAlmostEqual( v, expected[i*height + j], 5 )

	def testV2ff( self ) :

		expected = (
			0.50000, 0.51191, 0.52342, 0.53419, 0.54392, 0.55238, 0.55939, 0.56480, 0.56852, 0.57049,
			0.51607, 0.52798, 0.53948, 0.55024, 0.55994, 0.56837, 0.57533, 0.58069, 0.58433, 0.58621,
			0.53243, 0.54433, 0.55582, 0.56655, 0.57623, 0.58461, 0.59152, 0.59680, 0.60037, 0.60215,
			0.54931, 0.56117, 0.57262, 0.58331, 0.59294, 0.60127, 0.60811, 0.61331, 0.61678, 0.61846,
			0.56684, 0.57863, 0.59001, 0.60063, 0.61018, 0.61843, 0.62518, 0.63029, 0.63366, 0.63522,
			0.58507, 0.59676, 0.60804, 0.61855, 0.62799, 0.63613, 0.64277, 0.64776, 0.65100, 0.65244,
			0.60400, 0.61555, 0.62668, 0.63704, 0.64634, 0.65434, 0.66083, 0.66568, 0.66878, 0.67008,
			0.62359, 0.63494, 0.64587, 0.65605, 0.66516, 0.67297, 0.67929, 0.68397, 0.68691, 0.68805,
			0.64372, 0.65482, 0.66551, 0.67545, 0.68433, 0.69191, 0.69802, 0.70250, 0.70525, 0.70623,
			0.66426, 0.67506, 0.68545, 0.69509, 0.70369, 0.71102, 0.71687, 0.72112, 0.72367, 0.72445,
		)

		n = IECore.PerlinNoiseV2ff()

		width = 10
		height = 10

		for i in range( 0, height ) :
			for j in range( 0, width ) :
				f = 0.5 + n.noise( IECore.V2f( i/50.0, j/50.0 ) )
				self.assertAlmostEqual( f, expected[i*height + j], 4 )

	def testV3ff( self ) :

		expected = (
			(
				0.50000, 0.51154, 0.52333, 0.53558, 0.54839, 0.56183, 0.57592, 0.59062, 0.60585, 0.62153,
				0.51018, 0.52172, 0.53352, 0.54577, 0.55859, 0.57205, 0.58616, 0.60089, 0.61617, 0.63189,
				0.52047, 0.53202, 0.54382, 0.55608, 0.56891, 0.58239, 0.59653, 0.61130, 0.62662, 0.64240,
				0.53094, 0.54250, 0.55431, 0.56659, 0.57944, 0.59295, 0.60713, 0.62193, 0.63731, 0.65314,
				0.54163, 0.55321, 0.56504, 0.57734, 0.59023, 0.60377, 0.61799, 0.63285, 0.64828, 0.66418,
				0.55254, 0.56415, 0.57602, 0.58835, 0.60128, 0.61487, 0.62914, 0.64406, 0.65957, 0.67555,
				0.56365, 0.57530, 0.58721, 0.59960, 0.61258, 0.62623, 0.64057, 0.65557, 0.67115, 0.68722,
				0.57491, 0.58661, 0.59858, 0.61103, 0.62408, 0.63781, 0.65223, 0.66732, 0.68300, 0.69918,
				0.58624, 0.59802, 0.61007, 0.62259, 0.63573, 0.64955, 0.66407, 0.67926, 0.69506, 0.71136,
				0.59758, 0.60944, 0.62158, 0.63421, 0.64744, 0.66137, 0.67601, 0.69132, 0.70725, 0.72368,
			),
			(
				0.56356, 0.57512, 0.58693, 0.59914, 0.61188, 0.62518, 0.63905, 0.65345, 0.66831, 0.68351,
				0.57376, 0.58532, 0.59713, 0.60935, 0.62209, 0.63541, 0.64931, 0.66374, 0.67863, 0.69388,
				0.58404, 0.59562, 0.60743, 0.61966, 0.63242, 0.64575, 0.65967, 0.67414, 0.68907, 0.70437,
				0.59448, 0.60606, 0.61789, 0.63013, 0.64291, 0.65627, 0.67022, 0.68472, 0.69971, 0.71506,
				0.60507, 0.61667, 0.62852, 0.64079, 0.65359, 0.66699, 0.68098, 0.69553, 0.71057, 0.72599,
				0.61582, 0.62745, 0.63933, 0.65163, 0.66447, 0.67791, 0.69196, 0.70657, 0.72167, 0.73717,
				0.62668, 0.63836, 0.65028, 0.66263, 0.67552, 0.68902, 0.70313, 0.71781, 0.73300, 0.74857,
				0.63761, 0.64934, 0.66131, 0.67372, 0.68669, 0.70026, 0.71445, 0.72922, 0.74449, 0.76017,
				0.64853, 0.66032, 0.67237, 0.68486, 0.69790, 0.71156, 0.72584, 0.74071, 0.75610, 0.77189,
				0.65934, 0.67122, 0.68336, 0.69593, 0.70907, 0.72284, 0.73723, 0.75222, 0.76773, 0.78365,
			),
			(
				0.62051, 0.63226, 0.64421, 0.65648, 0.66917, 0.68230, 0.69585, 0.70978, 0.72399, 0.73839,
				0.63084, 0.64259, 0.65454, 0.66682, 0.67951, 0.69265, 0.70622, 0.72016, 0.73440, 0.74882,
				0.64124, 0.65299, 0.66494, 0.67723, 0.68993, 0.70308, 0.71667, 0.73063, 0.74490, 0.75935,
				0.65174, 0.66350, 0.67546, 0.68776, 0.70048, 0.71364, 0.72725, 0.74124, 0.75554, 0.77003,
				0.66236, 0.67413, 0.68611, 0.69842, 0.71116, 0.72435, 0.73799, 0.75201, 0.76635, 0.78088,
				0.67307, 0.68487, 0.69686, 0.70920, 0.72197, 0.73519, 0.74887, 0.76293, 0.77732, 0.79190,
				0.68383, 0.69566, 0.70769, 0.72006, 0.73287, 0.74613, 0.75985, 0.77397, 0.78841, 0.80306,
				0.69457, 0.70644, 0.71851, 0.73093, 0.74379, 0.75711, 0.77089, 0.78507, 0.79958, 0.81431,
				0.70523, 0.71715, 0.72927, 0.74175, 0.75467, 0.76805, 0.78190, 0.79617, 0.81076, 0.82557,
				0.71570, 0.72768, 0.73987, 0.75242, 0.76541, 0.77888, 0.79281, 0.80717, 0.82186, 0.83677,
			),
			(
				0.66013, 0.67228, 0.68454, 0.69701, 0.70971, 0.72264, 0.73576, 0.74900, 0.76227, 0.77545,
				0.67074, 0.68288, 0.69515, 0.70762, 0.72032, 0.73324, 0.74636, 0.75959, 0.77285, 0.78602,
				0.68140, 0.69354, 0.70581, 0.71827, 0.73097, 0.74390, 0.75701, 0.77024, 0.78349, 0.79665,
				0.69213, 0.70427, 0.71654, 0.72901, 0.74171, 0.75463, 0.76774, 0.78097, 0.79422, 0.80738,
				0.70292, 0.71507, 0.72734, 0.73981, 0.75252, 0.76545, 0.77856, 0.79179, 0.80504, 0.81820,
				0.71375, 0.72591, 0.73819, 0.75067, 0.76338, 0.77631, 0.78943, 0.80266, 0.81592, 0.82909,
				0.72457, 0.73674, 0.74902, 0.76151, 0.77423, 0.78718, 0.80031, 0.81356, 0.82683, 0.84001,
				0.73531, 0.74749, 0.75979, 0.77229, 0.78503, 0.79799, 0.81114, 0.82441, 0.83770, 0.85090,
				0.74590, 0.75809, 0.77040, 0.78292, 0.79568, 0.80867, 0.82184, 0.83513, 0.84846, 0.86169,
				0.75624, 0.76845, 0.78079, 0.79333, 0.80611, 0.81912, 0.83233, 0.84566, 0.85901, 0.87229,
			),
			(
				0.67356, 0.68628, 0.69903, 0.71181, 0.72459, 0.73733, 0.74994, 0.76235, 0.77444, 0.78612,
				0.68458, 0.69730, 0.71004, 0.72281, 0.73558, 0.74829, 0.76088, 0.77324, 0.78528, 0.79690,
				0.69563, 0.70834, 0.72108, 0.73384, 0.74660, 0.75928, 0.77183, 0.78415, 0.79614, 0.80769,
				0.70671, 0.71942, 0.73215, 0.74490, 0.75763, 0.77030, 0.78281, 0.79509, 0.80702, 0.81851,
				0.71780, 0.73050, 0.74322, 0.75596, 0.76867, 0.78130, 0.79378, 0.80602, 0.81790, 0.82932,
				0.72888, 0.74156, 0.75427, 0.76698, 0.77967, 0.79227, 0.80471, 0.81690, 0.82873, 0.84009,
				0.73989, 0.75255, 0.76522, 0.77791, 0.79057, 0.80314, 0.81554, 0.82768, 0.83946, 0.85076,
				0.75076, 0.76338, 0.77603, 0.78868, 0.80130, 0.81383, 0.82619, 0.83829, 0.85002, 0.86127,
				0.76141, 0.77400, 0.78660, 0.79921, 0.81179, 0.82428, 0.83660, 0.84865, 0.86033, 0.87153,
				0.77177, 0.78430, 0.79686, 0.80942, 0.82196, 0.83440, 0.84667, 0.85867, 0.87031, 0.88146,
			),
		)

		n = IECore.PerlinNoiseV3ff()

		width = 10
		height = 10

		for frame in range( 0, 5 ) :
			for i in range( 0, height ) :
				for j in range( 0, width ) :
					f = 0.5 + n.noise( IECore.V3f( i/50.0, j/50.0, frame/10.0 ) )
					self.assertAlmostEqual( f, expected[frame][i*height + j], 4 )

	def testV2fColor3f( self ) :

		rExpected = (
			0.50000, 0.48158, 0.46275, 0.44323, 0.42280, 0.40139, 0.37896, 0.35558, 0.33136, 0.30645,
			0.50798, 0.48956, 0.47073, 0.45119, 0.43075, 0.40930, 0.38682, 0.36336, 0.33904, 0.31401,
			0.51606, 0.49766, 0.47885, 0.45931, 0.43886, 0.41739, 0.39487, 0.37135, 0.34694, 0.32181,
			0.52431, 0.50596, 0.48720, 0.46770, 0.44727, 0.42580, 0.40327, 0.37971, 0.35525, 0.33003,
			0.53277, 0.51452, 0.49584, 0.47642, 0.45606, 0.43464, 0.41213, 0.38858, 0.36409, 0.33882,
			0.54145, 0.52335, 0.50481, 0.48553, 0.46529, 0.44397, 0.42154, 0.39804, 0.37357, 0.34828,
			0.55033, 0.53244, 0.51412, 0.49504, 0.47498, 0.45382, 0.43152, 0.40813, 0.38373, 0.35848,
			0.55937, 0.54178, 0.52374, 0.50493, 0.48512, 0.46419, 0.44210, 0.41887, 0.39461, 0.36945,
			0.56854, 0.55130, 0.53363, 0.51516, 0.49569, 0.47507, 0.45325, 0.43026, 0.40620, 0.38119,
			0.57775, 0.56097, 0.54373, 0.52570, 0.50663, 0.48640, 0.46494, 0.44226, 0.41847, 0.39368,
		)

		gExpected = (
			0.50000, 0.51006, 0.52036, 0.53106, 0.54227, 0.55405, 0.56642, 0.57935, 0.59277, 0.60660,
			0.48275, 0.49282, 0.50313, 0.51388, 0.52517, 0.53709, 0.54966, 0.56284, 0.57659, 0.59082,
			0.46584, 0.47591, 0.48624, 0.49703, 0.50842, 0.52047, 0.53322, 0.54666, 0.56073, 0.57536,
			0.44956, 0.45964, 0.46999, 0.48083, 0.49230, 0.50448, 0.51742, 0.53110, 0.54549, 0.56049,
			0.43418, 0.44427, 0.45465, 0.46554, 0.47709, 0.48940, 0.50251, 0.51642, 0.53110, 0.54646,
			0.41994, 0.43004, 0.44045, 0.45138, 0.46301, 0.47544, 0.48872, 0.50285, 0.51779, 0.53349,
			0.40702, 0.41715, 0.42758, 0.43857, 0.45027, 0.46281, 0.47624, 0.49056, 0.50575, 0.52174,
			0.39560, 0.40575, 0.41622, 0.42726, 0.43903, 0.45167, 0.46523, 0.47972, 0.49513, 0.51137,
			0.38580, 0.39599, 0.40649, 0.41758, 0.42942, 0.44215, 0.45582, 0.47046, 0.48604, 0.50250,
			0.37772, 0.38795, 0.39850, 0.40964, 0.42154, 0.43434, 0.44811, 0.46287, 0.47859, 0.49522,
		)

		bExpected = (
			0.50000, 0.51757, 0.53523, 0.55305, 0.57101, 0.58909, 0.60722, 0.62530, 0.64321, 0.66082,
			0.49035, 0.50792, 0.52560, 0.54345, 0.56148, 0.57968, 0.59797, 0.61627, 0.63446, 0.65241,
			0.48039, 0.49794, 0.51562, 0.53350, 0.55159, 0.56989, 0.58834, 0.60685, 0.62531, 0.64359,
			0.46989, 0.48740, 0.50505, 0.52293, 0.54106, 0.55944, 0.57802, 0.59672, 0.61543, 0.63404,
			0.45868, 0.47612, 0.49371, 0.51155, 0.52968, 0.54811, 0.56679, 0.58565, 0.60460, 0.62351,
			0.44668, 0.46399, 0.48147, 0.49923, 0.51732, 0.53576, 0.55451, 0.57350, 0.59265, 0.61183,
			0.43383, 0.45097, 0.46830, 0.48592, 0.50392, 0.52232, 0.54109, 0.56017, 0.57948, 0.59889,
			0.42017, 0.43707, 0.45418, 0.47161, 0.48947, 0.50777, 0.52651, 0.54563, 0.56505, 0.58467,
			0.40573, 0.42234, 0.43916, 0.45635, 0.47400, 0.49215, 0.51080, 0.52991, 0.54940, 0.56917,
			0.39062, 0.40686, 0.42334, 0.44021, 0.45758, 0.47552, 0.49402, 0.51306, 0.53256, 0.55243,
		)

		n = IECore.PerlinNoiseV2fColor3f()

		width = 10
		height = 10

		for i in range( 0, height ) :
			for j in range( 0, width ) :
				c = n.noise( IECore.V2f( i/50.0, j/50.0 ) )
				self.assertAlmostEqual( c.r + 0.5, rExpected[i*height + j], 4 )
				self.assertAlmostEqual( c.g + 0.5, gExpected[i*height + j], 4 )
				self.assertAlmostEqual( c.b + 0.5, bExpected[i*height + j], 4 )

#	def testSpeed( self ) :
#
#		numPoints = 100000
#		p = IECore.V3fVectorData( numPoints )
#		random.seed( 0 )
#		for i in xrange( 0, numPoints ) :
#			p[i] = IECore.V3f( random.uniform( -1000, 1000 ), random.uniform( -1000, 1000 ), random.uniform( -1000, 1000 ))
#		v = IECore.FloatVectorData( numPoints )
#
#		n = IECore.PerlinNoiseV3ff()
#		t = IECore.Timer( True )
#		for i in range( 0, 200 ) :
#			vv = n.noiseVector( p, v )
#
#		print t.stop()
#		self.assert_( vv.isSame( v ) )

		# results
		######################################################
		# initial implementation (better weight interpolation)
		######################################################
		#
		#	10.82
		#	10.54
		#	10.76
		#	10.91
		#	10.4		10.686
		#
		######################################################
		# cheaper weight interpolation
		######################################################
		#
		#	9.78
		#	9.52
		#	9.79
		#	9.71
		#	9.73		9.706
		#
		######################################################
		# fast floor function
		######################################################
		#
		#	9.54
		#	9.52
		#	9.26
		#	9.32
		#	9.57		9.442
		#
		######################################################
		# static weight function
		######################################################
		#
		#	9.33
		#	9.15
		#	9.36
		#	9.39
		#	9.7			9.386
		#
		######################################################
		# inline weight function
		######################################################
		#
		#	9.49
		#	9.36
		#	9.24
		#	9.15
		#	9.31		9.31
		#
		######################################################
		# inline noise() and noiseWalk()
		######################################################
		#
		#	7.97
		#	8.08
		#	8.06
		#	8.07
		#	8.06		8.048
		#
		######################################################
		# inline VectorOps
		######################################################
		#
		#	8.01
		#	8.05
		#	7.92
		#	7.96
		#	7.96		7.98
		#
		######################################################
		# gradient in contiguous memory
		######################################################
		#
		#	7.84
		#	7.69
		#	7.85
		#	7.78
		#	7.84		7.8
		#
		######################################################
		# timings made while fixing the bug caused by
		# fastFloatFloor bugs when compiled with optimisiation.
		######################################################
		#
		# failing fast floor function
		#
		# 9.77
		# 9.76
		# 9.71
		# 9.69
		# 9.75
		#
		# passing floor function
		#
		# 8.79
		# 8.83
		# 8.84
		# 8.83
		# 8.84
		#
		# fixed fast floor function
		#
		# 7.2
		# 7.19
		# 7.15
		# 7.15
		# 7.18
		#
		######################################################

	def testRepeatability( self ) :

		n = IECore.PerlinNoiseV2ff( 10 )
		n2 = IECore.PerlinNoiseV2ff( 10 )

		width = 200
		height = 200

		for i in range( 0, height ) :
			for j in range( 0, width ) :
				self.assertAlmostEqual( n.noise( IECore.V2f( i/50.0, j/50.0 ) ), n2.noise( IECore.V2f( i/50.0, j/50.0 ) ), 10 )


	def testFilterWidth( self ) :

		n = IECore.PerlinNoiseV2ff( 0 )

		for i in range( 1, 50 ) :
			for j in range( 1, 50 ) :
				p = IECore.V2f( i/50.0, j/50.0 )
				self.failUnless( n.noise( p ) != 0 )
				self.failUnless( n.noise( p, 0.5 ) != 0 )
				self.failUnless( n.noise( p, 0.6 ) == 0 )
				self.failUnless( n( p ) != 0 )
				self.failUnless( n( p, 0.5 ) != 0 )
				self.failUnless( n( p, 0.6 ) == 0 )

if __name__ == "__main__":
	unittest.main()


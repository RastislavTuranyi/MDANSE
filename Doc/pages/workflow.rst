
.. _workflow-of-analysis:

Workflow of the Analysis
========================

Most analysis jobs offered by MDANSE follow the same pattern of execution:

Input
-----

Trajectory
^^^^^^^^^^

The trajectory must be in the MDANSE format, saved as a NetCDF file.

(Most likely
your trajectory is in whatever format was output by your preferred Molecular Dynamics
simulation software, and you need to convert it first. Once you have converted your
trajectory to the MDANSE NetCDF format, you can use it as input for all kinds of
analysis. See also :ref:`trajectory-converters`)

Frames
^^^^^^

It is not necessary to use all the time frames of your MD simulation. You can decide
to limit the range of simulation time, and reduce the number of the frames taken in that
range by increasing the step between them. Only the frames you selected will
be passed to the analysis. See also :ref:`param-frames`.

Atom selection
^^^^^^^^^^^^^^

Just as it is not necessary to include all the time frames in the analysis, it is also
possible to select only a subset of all the atoms present in the trajectory. Once you
have defined a selection, you can decide to run an analysis on the selected atoms, and
ignore the rest. This is useful if you are trying to determine which atoms contribute
to a specific feature in your signal. See also :ref:`param-atom-selection`.

Analysis
--------

The analysis is run in steps, iterating over parts of the trajectory.

If you chose to
determine the atom velocities by **interpolation**, it will be done at this stage.

The iterations over steps will produce partial results. This is where the specific
equations described in the documentation of an analysis type are applied.
The partial results will be combined into
the final result in the next step of the workflow.

Finalising
----------

At this stage the partial properties have been calculated, typically per atom type,
or per pair of atom types. They will now be combined into the final result.

Resolution
^^^^^^^^^^

If the analysis allows for applying instrumental resolution, it will be done first.
The resolution is enabled only for the analysis types which calculate an energy spectrum.
This is normally done by calculating a Fourier transform of a correlation function.
The resolution is applied by multiplying the time-dependent function by a window function
before applying the Fourier transform. The details are given in the section 
:ref:`param-instrument-resolution`.

Normalisation
^^^^^^^^^^^^^

If the analysis offers the option of normalising the results, it is done at this stage.
The normalisation is described in the section :ref:`param-normalize`.

Weighting
^^^^^^^^^

The partial properties calculated so far will now be combined using the weights
chosen by the user, as described in the section :ref:`param-weights`. Please remember
that the MDANSE GUI normally recommends the weighting scheme appropriate to the
type of analysis performed.

Writing output
--------------

All the output arrays created in the analysis are written to the filesystem in the
format chosen by the user. (If you intend to continue visualising the results within
the MDANSE GUI, you will have chosen the HDF5 format. If, however, you were planning
to process the results further using other software, then you have most likely picked
the ASCII output. See also :ref:`param-output-files`)

"""
Using Latch SDK workflow references to chain together two workflows
"""

import subprocess
from pathlib import Path

from latch import small_task, workflow
from latch.resources.launch_plan import LaunchPlan
from latch.types import LatchAuthor, LatchFile, LatchMetadata, LatchParameter

from flytekit.core.launch_plan import reference_launch_plan

@reference_launch_plan(
    project="4034",
    domain="development",
    name="wf.__init__.msa_wf",
    version="0.0.0-6a622d",
)
def msa_wf(fasta: LatchFile) -> LatchFile:
    ...

@reference_launch_plan(
    project="4034",
    domain="development",
    name="wf.__init__.maketree_wf",
    version="0.0.0-ee71be",
)
def maketree_wf(afa: LatchFile) -> LatchFile:
    ...


"""The metadata included here will be injected into your interface."""
metadata = LatchMetadata(
    display_name="MSA & Phylogenetic Tree Generation with MUSCLE",
    documentation="your-docs.dev",
    author=LatchAuthor(
        name="John von Neumann",
        email="hungarianpapi4@gmail.com",
        github="github.com/fluid-dynamix",
    ),
    repository="https://github.com/your-repo",
    license="MIT",
    parameters={
        "fasta": LatchParameter(
            display_name="FASTA File",
            description="Sequences to be aligned",
            batch_table_column=True,  # Show this parameter in batched mode.
        )
    },
    tags=[],
)

@workflow(metadata)
def msa_maketree_wf(fasta: LatchFile) -> LatchFile:
    """Description...

    markdown header
    ----

    Write some documentation about your workflow in
    markdown here:

    > Regular markdown constructs work as expected.

    # Heading

    * content1
    * content2
    """
    afa = msa_wf(fasta=fasta)
    return maketree_wf(afa=afa)


"""
Add test data with a LaunchPlan. Provide default values in a dictionary with
the parameter names as the keys. These default values will be available under
the 'Test Data' dropdown at console.latch.bio.
"""
LaunchPlan(
    msa_maketree_wf,
    "Test Data",
    {
        "fasta": LatchFile("s3://latch-public/test-data/4034/zika-tutorial/data/sequences.fasta")
    },
)

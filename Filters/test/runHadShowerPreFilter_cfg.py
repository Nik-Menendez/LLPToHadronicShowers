import FWCore.ParameterSet.Config as cms

process = cms.Process("SKIM")
# initialize  MessageLogger

process.load("FWCore.MessageService.MessageLogger_cfi")

process.source = cms.Source(
    "PoolSource",
    fileNames = cms.untracked.vstring("file:input.root")
)

process.maxEvents = cms.untracked.PSet ( input = cms.untracked.int32 ( 1000 ) )

process.myfilter = cms.EDFilter(
    "HadShowerPreFilter",
    CSCComparatorDigiProducer = cms.InputTag("simMuonCSCDigis","MuonCSCComparatorDigi"),
    CSCWireDigiProducer = cms.InputTag("simMuonCSCDigis","MuonCSCWireDigi")
)

process.filterPath = cms.Path(process.myfilter)

process.output = cms.OutputModule(
    "PoolOutputModule",
    fileName = cms.untracked.string( "Filter.root" ),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring("filterPath")
    )
)

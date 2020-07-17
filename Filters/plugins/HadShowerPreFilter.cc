// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/EDFilter.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Utilities/interface/EDGetToken.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/CSCDigi/interface/CSCWireDigiCollection.h"
#include "DataFormats/CSCDigi/interface/CSCComparatorDigiCollection.h"

//******************************************************************************
//                           Class declaration
//******************************************************************************

class HadShowerPreFilter : public edm::EDFilter
{
public:
  explicit HadShowerPreFilter(const edm::ParameterSet&);
  ~HadShowerPreFilter();

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

private:
  virtual void beginJob() ;
  virtual bool filter(edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
  int maxRing(int station);

  virtual void beginRun(edm::Run const&, edm::EventSetup const&);
  virtual void endRun(edm::Run const&, edm::EventSetup const&);
  virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);
  virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);

  //****************************************************************************
  //          RECO LEVEL VARIABLES, BRANCHES, COUNTERS AND SELECTORS
  //****************************************************************************

  // Labels to access
  edm::InputTag wireDigiProducer_;
  edm::InputTag compDigiProducer_;

  edm::EDGetTokenT<CSCWireDigiCollection> wireDigi_token_;
  edm::EDGetTokenT<CSCComparatorDigiCollection> compDigi_token_;
};

HadShowerPreFilter::HadShowerPreFilter(const edm::ParameterSet& iConfig)
{
  wireDigiProducer_ = iConfig.getParameter<edm::InputTag>("CSCWireDigiProducer");
  compDigiProducer_ = iConfig.getParameter<edm::InputTag>("CSCComparatorDigiProducer");

  wireDigi_token_ = consumes<CSCWireDigiCollection>(wireDigiProducer_);
  compDigi_token_ = consumes<CSCComparatorDigiCollection>(compDigiProducer_);
}


HadShowerPreFilter::~HadShowerPreFilter()
{
}

bool
HadShowerPreFilter::filter(edm::Event& ev, const edm::EventSetup& iSetup)
{
  using namespace edm;

  bool returnValue = false;


  edm::Handle<CSCWireDigiCollection> wireDigis;
  edm::Handle<CSCComparatorDigiCollection> compDigis;

  ev.getByToken(wireDigi_token_, wireDigis);
  ev.getByToken(compDigi_token_, compDigis);

  for (int endc = 1; endc <= 2; endc++) {
    for (int stat = 1; stat <= 4; stat++) {
      for (int ring = 1; ring <= maxRing(stat); ring++) {
        for (int cham = 1; cham <= 36; cham++) {
          // Calculate DetId.  0th layer means whole chamber.

          std::vector<CSCComparatorDigi> compV;
          for (int layr = 1; layr <= 6; layr++) {
            CSCDetId detid_layer(endc, stat, ring, cham, layr);
            const auto& crange = compDigis->get(detid_layer);
            for (auto digiIt = crange.first; digiIt != crange.second; digiIt++) {
              compV.push_back(*digiIt);
            }
            // ME1/1 case, also consider ME1/a hits
            if (stat == 1 and ring == 1) {
              CSCDetId detid_me1a(endc, stat, 4, cham, layr);
              const auto& crange = compDigis->get(detid_me1a);
              for (auto digiIt = crange.first; digiIt != crange.second; digiIt++) {
                compV.push_back(*digiIt);
              }
            }
          }

          // filter requires at least one chamber to have at least 30 comparator hits in the event
          if (compV.size() > 30) {
            returnValue = true;
          }
        }
      }
    }
  }
  return returnValue;
}


// ------------ method called once each job just before starting event loop  ------------
void
HadShowerPreFilter::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void
HadShowerPreFilter::endJob()
{
}

// ------------ method called when starting to processes a run  ------------
void
HadShowerPreFilter::beginRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void
HadShowerPreFilter::endRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void
HadShowerPreFilter::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void
HadShowerPreFilter::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
HadShowerPreFilter::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

int HadShowerPreFilter::maxRing(int station) {
  if (station == 1) {
    return 3;
  }
  return 2;
}

//Indentation change
//define this as a plug-in
DEFINE_FWK_MODULE(HadShowerPreFilter);

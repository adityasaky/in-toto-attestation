/*
 * Wrapper APIs for in-toto attestation ResourceDescriptor protos.
*/

package v1

import (
	"errors"
	
	"google.golang.org/protobuf/types/known/structpb"
)

func NewResourceDescriptorPb(name string, uri string,
	digest map[string]string, content []byte,
	downloadLocation string, mediaType string,
	annotations map[string]*structpb.Struct) (*ResourceDescriptor, error) {
	
	d := &ResourceDescriptor{
		Name:             name,
		Uri:              uri,
		Digest:           digest,
		Content:          content,
		DownloadLocation: downloadLocation,
		MediaType:        mediaType,
		Annotations:      annotations,
	}

	if !IsValidResourceDescriptor(d) {
		return nil, errors.New("malformed resource descriptor")
	}
	
	return d, nil
}

func IsValidResourceDescriptor(d *ResourceDescriptor) bool {
	// at least one of name, URI or digest are required
	if d.GetName() == "" && d.GetUri() == "" && len(d.GetDigest()) == 0 {
		return false
	}

	return true
}
